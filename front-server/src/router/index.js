import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'

import SignUpView from '@/views/accounts/SignUpView'
import LogInView from '@/views/accounts/LogInView'

import CommunityView from '@/views/community/Community.vue'
import ArticleCreateView from '@/views/community/ArticleCreate'
import ArticleDetailView from '@/views/community/ArticleDetail'
import CommentCreateView from '@/components/community/CommentCreate'

import ProductsView from '@/views/products/Products.vue'
// import ProductsListView from '@/views/products/ProductsList.vue'
// import ProductsDetail from '@/views/products/ProductsDetail.vue'
// import SaveProducts from '@/views/products/SaveProducts.vue'


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
    path: '/articles/:id/comments',
    name: 'CommentCreateView',
    component: CommentCreateView
  },
  // products
  {
    path: '/products',
    name: 'ProductsView',
    component: ProductsView
  },
  // { 
  //   path: '/products/deposit-products/', 
  //   name: 'ProductsListView',
  //   component: ProductsListView
  // },
  // { 
  //   path: '/products/deposit-products/:fin_prdt_cd', 
  //   component: ProductsDetail
  // },
  // { 
  //   path: '/products/saving-products/', 
  //   component: SaveProducts 
  // },


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
