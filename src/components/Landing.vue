<template lang="pug">

<div>
<b-container class="bv-example-row">
    <b-row>
    <h1 style="font-weight: 500"> fuse </h1> &nbsp;&nbsp; <h2 style="font-weight: 300"> a file upload web service</h2>

    </b-row>
    <div style="border: 1px solid gray; padding: 25px; border-radius: 5px;margin: 60px">
    <b-row>
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

    <b-row class="footer"><b-col>&copy;2018 Antonio Vivace. See the <a href="https://github.com/avivace/fuse">source </a>on GitHub.</b-col></b-row>
</b-container>
</div>
</template>

<script>

export default {
  name: 'Landing',
  data () {
    return {
      file: null,
      counter: 0,
      max: 100,
      uploadInProgress: false,
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
          console.dir(result.data);
        })
      }
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700');

.footer {
  font-size:0.9rem;
  font-family: 'Ubuntu';
}
h1, h2 {
  font-family: 'Ubuntu';
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
