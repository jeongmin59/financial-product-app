import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'

import Signup from '@/views/accounts/Signup.vue'
import Login from '@/views/accounts/Login.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  // 회원가입
  {
    path: '/accounts/signup/',
    name: 'Signup',
    component: Signup
  },
  // 로그인
  {
    path: '/accounts/login/',
    name: 'Login',
    component: Login
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
