import Vue from 'vue'
import VueRouter from 'vue-router'
import './plugins/vuetify'
import Review from './components/NewReview.vue'
import App from './App.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/professors', component: Review },
]

const router = new VueRouter({
  routes,
  mode: 'history'
})

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
