<template>

<div>
DOWNLOAD PAGE
{{ $route.params.id }}
</div>
</template>

<script>

export default {
  name: 'Download',
  data () {
    return {
      a : 0
    }
  },
  methods: {
    download() {
      setTimeout(function(){
        window.location = "http://localhost:5000/file/cae911"
      }, 1000)   
    },
  }
}
</script>