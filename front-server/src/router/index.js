import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '../views/MainView.vue'
import InterestView from '../views/Financial/InterestView.vue'
import CommunityView from '../views/Community/CommunityView.vue'
import ArticleCreate from '../components/Article/ArticleCreateView.vue'
import LogInView from '../views/Accounts/LogInView.vue'
import SignUpView from '../views/Accounts/SignUpView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'main',
    component: MainView
  },
  {
    path: '/interest',
    name: 'interest',
    component: InterestView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/article_create',
    name: 'ArticleCreate',
    component: ArticleCreate
  },
  {
    path: 'login',
    name: 'LogInView',
    component: LogInView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
