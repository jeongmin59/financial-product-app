import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles: [],
    comments: [],
    token: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    // COMMUNITY
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    GET_COMMENTS(state, comments) {
      state.comments = comments
    },
    
    // signup & login -> 완료하면 토큰 발급
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'CommunityView'}) // store/index.js $router 접근 불가 -> import를 해야함
    }
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'GET',
        url: `${API_URL}/articles/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then((res) => {
        // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getComments(context) {
      axios({
        method: 'GET',
        url: `${API_URL}/articles/${ this.$route.params.id }/comments/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then((res) => {
          context.commit('GET_COMMENTS', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },

    // ACCOUNTS
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'POST',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
        })
        .then((res) => {
          // console.log(res)
          // context.commit('SIGN_UP', res.data.key)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    login(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: 'POST',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        })
      .catch((err) => console.log(err))
    }
  },
  modules: {
  }
})