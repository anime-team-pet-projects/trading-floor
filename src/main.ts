import { createApp } from 'vue';
import { createPinia } from 'pinia';
import router from '@/router';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import '@/styles/index.scss';

import App from './App.vue';

const app = createApp(App);

app.use(createPinia()).use(ElementPlus).use(router);

app.mount('#app');
