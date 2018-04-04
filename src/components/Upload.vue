<template>

<div>
    <b-row v-if="uploadCompleted">
      {{ uploadedFileURL }}
    </b-row>
    <b-row v-if="!uploadCompleted">
        <b-col  lg=8><b-form-file v-model="file" :state="Boolean(file)" placeholder="Choose a file..."></b-form-file></b-col>
        <b-col  md="auto"><b-button variant="warning" @click="upload">Upload</b-button></b-col>
    </b-row>
    <br>
    <b-row>
    <b-col>
    <b-progress v-if="uploadInProgress" height="2rem" :value="counter" :max="max" show-progress animated></b-progress>
    </b-col>
    </b-row>
</div>

</template>

<script>

export default {
  name: 'Upload',
  data () {
    return {
      API_ENDPOINT: process.env.API_ENDPOINT,
      BASE_DOMAIN: process.env.BASE_DOMAIN,
      file: null,
      counter: 0,
      max: 100,
      uploadInProgress: false,
      uploadedFileURL: '',
      uploadCompleted: false
    }
  },
  methods: {
    updateProgressBar(progress) {
      console.log(percentCompleted)
    },
    upload(e) {
      console.log(this.file)
      if (this.file){
        this.uploadInProgress = true;
        var formdata = new FormData();
        formdata.append('file', this.file)
        const config = {
          headers: {'Content-Type':'multipart/form-data'},
          onUploadProgress: progressEvent => {
            this.counter = Math.floor((progressEvent.loaded * 100) / progressEvent.total);
          }
        }
        this.$axios.post("http://localhost:5000/upload", formdata, config).then(result => {
          this.uploadedFileURL = result.data;
          this.uploadCompleted = true;
          this.uploadInProgress = false;
          console.dir(result.data);
        })
      }
    }
  }
}
</script>

<style>

</style>
