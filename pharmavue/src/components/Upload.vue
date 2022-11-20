<template>
    <div class="">
        <div class="">
            <div class="form-header">
                <h1 class="">Choose an image</h1>
            </div>
            <div class="form-body">
                <form @submit="uploadFile">
                    <div class="">
                        <div class="">
                            <input 
                                type="file" 
                                id="documentUpload" 
                                name="image" 
                                class="hover:cursor-pointer" 
                                accept="image/png, image/jpeg"
                                @change="onChange"
                                required 
                            />
                        </div>
                        <div class="form-submit">
                            <input 
                                type="submit" 
                                value="Upload" 
                                class="border-2 rounded-lg px-2 py-px hover:cursor-pointer submit-btn"
                            />
                        </div>
                    </div>
                </form>
            </div>
        </div>
        <div 
            class="modal" 
            v-show="imageUpload"
        >
            <div class="modal-content">
                <div class="modal-header">
                    <h2 class="">Image Preview</h2>
                </div>
                <div class="modal-body">
                    <img :src="image" alt="Uploaded image" />
                </div>
                <div class="modal-footer">
                    <button class="modal-close" @click="closeModal">
                        Close
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Upload',
        mounted () {
            window.onclick = function(event) {
                if (event.target.className === "modal") {
                    this.imageUpload = false;
                    event.target.style.display = "none";
                }
            }
        },
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

                console.log("target::", e.target.className);

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
<style>
    .modal {
        position: fixed;
        z-index: 1;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0,0,0,0.4);
        left: 0;
        top: 0;
        margin-left: auto;
        padding-top: 50px;
    }

    .modal-content {
        position: relative;
        background-color: #FFF;
        margin: auto;
        width: 60%;
        border-radius: 20px;
        padding: 10px;
    }

    .modal-header {
        padding: 10px;
    }

    .modal-body {
        padding: 10px;
    }

    .modal-footer {
        padding: 10px;
    }

    .modal-close {
        padding-left: 5px;
        padding-right: 5px;
        border-radius: 5px;
        background-color: #5F8D4E;
    }

    .submit-btn {
        padding: 5px;
        border-radius: 10px;
        background-color: #A4BE7B;
    }

    .form-body,.form-submit {
        margin-top: 10px;
    }

    .submit-btn:hover {
        cursor: pointer;
    }
</style>