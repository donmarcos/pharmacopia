<template>
    <div class="home">
        <img alt="Vue logo" src="../assets/pharmacopialogo.png">
    </div>
    <div class="file-upload">
        <div class="file-upload_area">
            <div class="">
                <h1 class="">Upload Your Prescription</h1>
            </div>
            <div>
                <form @submit="uploadFile">
                    <div class="">
                        <div class="p-4">
                            <input 
                                type="file" 
                                id="documentUpload" 
                                name="image" 
                                class="hover:cursor-pointer" 
                                accept="image/png, image/jpeg"
                                @change="onChange"
                            />
                        </div>
                        <div class="">
                            <input 
                                type="submit" 
                                value="Upload" 
                                class="border-2 rounded-lg px-2 py-px hover:cursor-pointer"
                            />
                        </div>
                    </div>
                </form>
            </div>
        </div>
        <div 
            class="" 
            v-show="imageUpload"
            @click="closeModal"
        >
           <br />
            <div class="">
                <h2 class="">Preview</h2>
                <img :src="image" alt="Uploaded image" />
                <button class="" @click="closeModal">
                    Close
                </button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Upload',
        data() {
            return { 
                imageUpload: false,
                image: ''
            };
        },
        methods: {
            onChange(e) {
                this.image = '';
                this.imageUpload = false;

                let files = e.target.files || e.dataTransfer.files;

                if (!files.length) {
                    return;
                }

                this.setImage(files[0]);
                // this.formData.append('file', files[0]);
            },
            setImage(file) {
                let reader = new FileReader();

                reader.onload = (e) => {
                    this.image = e.target.result;
                    this.imageUpload = true;
                    console.log(this.image);
                }

                reader.readAsDataURL(file);
            },
            closeModal() {
                this.imageUpload = false;
                /* console.log(`closeModal function called ${this.imageUpload}`) */
            },
            uploadFile: async function (e) {
                e.preventDefault();

                console.log("target::", e);

                let formData = new FormData(e.target);

                if (this.image !== '') {
                    console.log(formData.get('image'));
                    try {
                        const response = await fetch(
                            'http://localhost:4000/api/upload',
                            {
                                method: 'POST',
                                body: formData
                            }

                        );

                        console.log(response);
                    } catch (error) {
                        console.log(error.message);
                    }
                }
            }
        }
    }
</script>

<style scoped>
.file-upload {
    height: 100vh;
    width: 100%;
    display: flex;
    align-items: flex-start;
    justify-content: center;
}

.file-upload .file-upload__area {
    width: 600px;
    min-height: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px dashed #ccc;
    margin-top: 40px;
}
</style>
