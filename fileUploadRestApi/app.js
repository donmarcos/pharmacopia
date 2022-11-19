const http = require('http');
const express = require("express");
const multer = require("multer");
const multerS3 = require("multer-s3-v2")
const AWS = require('aws-sdk')
const cors = require('cors')

const app = express();
app.use(cors());
app.use(express.json());

const s3 = new AWS.S3({
    accessKeyId: '<Enter you access key>',
    secretAccessKey: '<Enter your secret key>'
});

const uploadS3 = multer({
    storage: multerS3({
        s3: s3,
        bucket: '<Enter your bucket name>',
        metadata: (req, file, callBack) => {
            callBack(null, {fieldName: file.fieldname})
        },
        key: (req, file, callBack) => {
            callBack(null, file.originalname)
        }
    })
});

app.post("/api/upload",  uploadS3.single('image'), async (req, res) => {
    console.log(req.body);
    return res.status(200).send('OK')
});

const server = http.createServer(app);

server.listen(process.env.PORT || 4000, () => {
  console.log(`Server running on port ${4000}`);
});
