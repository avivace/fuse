<template>
<div id="app">
	<b-container>
	<b-row>
	<h1 style="font-weight: 500"> fuse </h1> &nbsp;&nbsp; <h2 style="font-weight: 300"> a file upload web service</h2>
	</b-row>
	<div style="border: 1px solid gray; padding: 25px; border-radius: 5px;margin: 60px">
		<router-view/>
	</div>
	<b-row class="footer"><b-col>&copy;2018 Antonio Vivace. See the <a href="https://github.com/avivace/fuse">source </a>on GitHub.</b-col></b-row>
	</b-container>
</div>
</template>

<script>
export default {
	name: 'App'
}
</script>

<style>

#app {
	font-family: 'Avenir', Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;

	color: #2c3e50;
	margin-top: 40px;
}
.progress-bar {
	font-size: 1.5rem;
}

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
