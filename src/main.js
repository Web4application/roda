import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import { ethers } from 'ethers'
import './styles/theme.css'

const app = createApp(App)
app.use(createPinia())
app.use(router)
app.config.globalProperties.$ethers = ethers
app.mount('#app')