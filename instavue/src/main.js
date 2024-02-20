import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'

import { createRouter, createWebHistory } from 'vue-router'; // 수정된 부분
import AnalysisPage from './AnalysisPage.vue'

loadFonts()

const routes = [
  {
    path: '/'
  },{
    path:'/analysis',
    component: AnalysisPage,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

createApp(App)
  .use(vuetify)
  .use(router) // 수정된 부분
  .mount('#app');
