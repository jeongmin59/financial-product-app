import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'

import SignUpView from '@/views/accounts/SignUpView'
import LogInView from '@/views/accounts/LogInView'

import CommunityView from '@/views/community/Community.vue'
import ArticleCreateView from '@/views/community/ArticleCreate'
import ArticleDetailView from '@/views/community/ArticleDetail'

import CommentCreateView from '@/components/community/CommentCreate'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  // accounts
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
  // community
  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView
  },
  {
    path: '/articles',
    name: 'ArticleCreateView',
    component: ArticleCreateView
  },
  {
    path: '/articles/:id',
    name: 'ArticleDetailView',
    component: ArticleDetailView,
  },
  {
    path: '/articles/:id/comment',
    name: 'CommentCreateView',
    component: CommentCreateView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
