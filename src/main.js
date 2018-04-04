// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueRouter from 'vue-router'

import App from './App'
import Upload from './components/Upload'
import Download from './components/Download'

import axios from 'axios';
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(VueRouter)
Vue.use(BootstrapVue);
Vue.prototype.$axios = axios.create();
Vue.config.productionTip = false

const routes = [
	{ path: '/', component: Upload },
	{ path: '/download/:id', component: Download}
]

const router = new VueRouter({
	routes // short for `routes: routes`
})

/* eslint-disable no-new */
new Vue({
  router,
  el: '#app',
  render: h => h(App)
})
