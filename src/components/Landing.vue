<template lang="pug">
<div>
<form action="/upload" method=post enctype=multipart/form-data>
<p><input type=file name=file>
<input type=submit value=Upload></p></form> 
</div>
</template>

<script>
export default {
  name: 'Landing',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
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
