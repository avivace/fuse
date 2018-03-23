<template lang="pug">

<div>
  h1 File Upload
  h1 {{msg}}
<input id="input" ref="fileInput" type="file">
<button @click="upload"> Upload </button>
</div>

</template>

<script>
export default {
  name: 'Landing',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  methods: {
    upload(e) {
      if (this.$refs.fileInput.files[0]){
        var formdata = new FormData();
        formdata.append('file', this.$refs.fileInput.files[0])
        const config = {
          headers : {'Content-Type':'multipart/form-data'}
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
