<template>

<div>
    <b-row v-if="!uploadCompleted">
        <b-col  lg=8><b-form-file v-model="file" :state="Boolean(file)" placeholder="Choose a file..."></b-form-file></b-col>
        <b-col  md="auto"><b-button variant="warning" @click="upload">Upload</b-button></b-col>
    </b-row>
   
    <b-row>
    <b-col v-if="uploadInProgress">
    <br>
    <b-progress  height="2rem" :value="counter" :max="max" show-progress animated></b-progress>
    </b-col>
    </b-row>
    <b-form v-if="uploadCompleted" inline>
    		Upload completed. Here's your link to share:&nbsp;&nbsp;
    		    <b-form-textarea @click.native="$event.target.select()" @focus.native="$event.target.select()"
                     :value="downloadURL"
							readonly
							no-resize>
    			</b-form-textarea>
    </b-form>
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
      uploadCompleted: false,
      downloadURL: ''
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
          this.downloadURL = process.env.BASE_DOMAIN+'/#/download/'+result.data['uploadUUID'];
          console.dir(result.data);
        })
      }
    }
  }
}
</script>

<style>
.form-inline .form-control {
	width: 60%;
	height: 3.1rem;
	font-family: 'Ubuntu Mono', monospace;
	font-size:1.5rem;
}
</style>
