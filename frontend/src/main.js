// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Navibar from './components/Navibar'
import router from './router'
import App from './App'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.config.productionTip = false

/* eslint-disable*/
new Vue({
   el: '#app',
   router,
   components: { App },
   template: '<App/>'
 })
new Vue({
  el: '#navibar',
  router,
  components: { Navibar },
  template: '<Navibar/>'
})
