<template lang="pug">

<div>
  h1 File Upload
  h1 {{msg}}


<b-form-file v-model="file" :state="Boolean(file)" placeholder="Choose a file..."></b-form-file>
<b-button @click="upload">Upload</b-button>
<b-progress :value="counter" :max="max" show-progress animated></b-progress>
</div>
</template>

<script>
export default {
  name: 'Landing',
  data () {
    return {
      file: null,
      msg: 'Welcome to Your Vue.js App',
      counter: 0,
      max: 100
    }
  },
  methods: {
    updateProgressBar(progress) {
      console.log(percentCompleted)
    },
    upload(e) {
      console.log(this.file)
      if (this.file){
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
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
