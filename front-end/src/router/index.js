import { createRouter, createWebHistory } from 'vue-router'
import Thingsview from '../views/Thingsview.vue'
import SignUpview from '../views/SignUpview.vue'
import SignInview from '../views/SignInview.vue'


const router = createRouter({
  history: createWebHistory(),
  routes: [
    {name: 'Things', path: '/', component: Thingsview },
    {name: 'SignUp', path: '/sign-up', component: SignUpview },
    {name: 'SignIn', path: '/sign-in', component: SignInview },
  ]
})

export default router
