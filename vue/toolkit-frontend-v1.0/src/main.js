import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'
import axios from 'axios'
import VueAxios from "vue-axios";
import router from './router/index.js'


Vue.config.productionTip = false
// 全局设置 axios 发送请求带上cookie
axios.defaults.withCredentials = true

Vue.use(VueAxios, axios)
Vue.use(ElementUI);

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
