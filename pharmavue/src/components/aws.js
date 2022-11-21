const aws = require('aws-sdk');
// const axios = require('axios');
import axios from 'axios'

aws.config.update({
  secretAccessKey: process.env.VUE_APP_AWS_SECRET_ACCESS_KEY,
  accessKeyId: process.env.VUE_APP_AWS_ACCESS_KEY,
})

export const s3 = new aws.S3({
  signatureVersion: 'v4',
  region: process.env.VUE_APP_AWS_REGION,
})

export const singleUpload = (file, folder) => {
  console.log(folder)
  const key = Date.now() + '-' + file.name.replace(/\s/g, '-')
  console.log("bucket ", process.env.VUE_APP_AWS_BUCKET)
  console.log("file type", file.type);
  const params = {
    Bucket: process.env.VUE_APP_AWS_BUCKET,
    Key: key,
    Expires: 10,
    ContentType: file.type,
  }
  const url = s3.getSignedUrl('putObject', params)
   return axios.put(url, file, {
      headers: {
        'Content-Type': file.type,
      },
    })
    .then(result => {
      const bucketUrl = decodeURIComponent(result.request.responseURL).split(
        key
      )[0]
      result.file = file
      result.key = key
      result.fullPath = bucketUrl + key
      return result
    })
    .catch(err => {
      // TODO: error handling
      console.log(err)
    })
}

export const procFile = (file) => {
      console.log("aws processing file ", file)
       const res =  axios.post('https://k6hdpt4e4diw4to47ojogmv7m40blyku.lambda-url.us-west-2.on.aws/', {
     object_name: file,
 });
 console.log(res);
}


export const deleteObjectByKey = key => {
  const params = {
    Bucket: process.env.VUE_APP_AWS_BUCKET,
    Key: key,
  }
  const data = s3.deleteObject(params).promise()

  return data
}
