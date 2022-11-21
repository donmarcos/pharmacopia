<template>
    <div class="home">
        <img alt="Vue logo" src="../assets/pharmacopialogo.png">
    </div>
    <div>
        <file-pond ref="pond" :server="{
            process: (fieldName, file, metadata, load, error, progress, abort) => {
                uploadFile(file, metadata, load, error, progress, abort)
            },
        }" @removefile="onRemoveFile" />
    </div>
</template>

<script>
import vueFilePond from 'vue-filepond'
import FilePondPluginFileValidateType from 'filepond-plugin-file-validate-type'
import FilePondPluginImagePreview from 'filepond-plugin-image-preview'

const FilePond = vueFilePond(
    FilePondPluginFileValidateType,
    FilePondPluginImagePreview
);

import axios from 'axios'
import { singleUpload, deleteObjectByKey } from './aws'

export default {
    name: 'Upload',
    components: {
        FilePond,
    },
    data() {
        return {
            imageUpload: false,
            image: ''
        };
    },
    methods: {
        async uploadFile(file, metadata, load, error, progress, abort) {
            const result = await singleUpload(
                file,
                this.$route.params.teamSlug // folder of the file, you should change it to your variable or a string
            )
            if (result.status === 200) {
                // Handle storing it to your database here
                load(file) // Let FilePond know the processing is done
            } else {
                error() // Let FilePond know the upload was unsuccessful
            }
            return {
                abort: () => {
                    // This function is entered if the user has tapped the cancel button
                    // Let FilePond know the request has been cancelled
                    abort()
                },
            }
        },
        async onRemoveFile(event) {
            let url = this.$route.params.teamSlug + '/' + event.file.name // event.file.name has only the name after the slash / so the actual filename
            const res = await deleteObjectByKey(url)
            if (
                res.$response.httpResponse.statusCode >= 200 &&
                res.$response.httpResponse.statusCode < 300
            ) {
                // here remove data from database too
            }
        },

    }
}
</script>

<style scoped>

</style>
