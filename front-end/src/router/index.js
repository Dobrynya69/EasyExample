import { createRouter, createWebHistory } from 'vue-router'
import Thingsview from '../views/Thingsview.vue'
import ItemsList from '../components/v-ItemsList.vue'
import SignUpview from '../views/SignUpview.vue'
import SignInview from '../views/SignInview.vue'


const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      name: 'Things', 
      path: '/', 
      component: Thingsview,
    },
  ]
})

export default router 
