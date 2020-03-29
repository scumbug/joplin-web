// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
// https://github.com/mzabriskie/axios
import axios from 'axios'
// https://github.com/vuejs/vue-router/
import VueRouter from 'vue-router'
// https://github.com/bootstrap-vue/bootstrap-vue
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import moment from 'moment'

import router from './router'
import store from './store'

import App from './App.vue'

Vue.prototype.moment = moment

Vue.use(VueRouter)
Vue.use(BootstrapVue)

window.Cookies = require('js-cookie')
// eslint-disable-next-line
let csrftoken = Cookies.get('csrftoken')

axios.defaults.headers.common.cookiename = 'csrftoken'
axios.defaults.headers.common['X-CSRFToken'] = csrftoken
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*'

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
