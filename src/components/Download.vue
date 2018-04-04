<template>

<div>
<h3>Downloading your file...</h3>
You requested the resource <code>{{ $route.params.id }}</code>
</div>
</template>

<script>

export default {
  name: 'Download',
  data () {
    return {
      a : ''
    }
  },
  methods: {
    download() {
      setTimeout(() => {
			window.location = "http://localhost:5000/file/"+this.$route.params.id
      }, 2000)
    },
  },
  mounted() {
  	this.download()
  }
}
</script>
