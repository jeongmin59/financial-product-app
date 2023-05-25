import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
// import vuetify from './plugins/vuetify'
import "./assets/fonts.css"

Vue.config.productionTip = false

new Vue({
  store,
  router,
  // vuetify,
  render: h => h(App)
}).$mount('#app')

