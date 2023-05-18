import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

const API_URL = 'http://127.0.0.1:8000/'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles: [
    ],
    token: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    SAVE_TOKEN(state, token) {
      // state.token = token //token 저장
      state.token = localStorage.getItem('jwt')
      state.isLogin = true
      state.username = token.username
      console.log(token)
      router.push({name : 'App'})
      console.log(this.isLogin)
    }
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'GET',
        url: `${API_URL}/articles/`,
        headers: {
          Authorization: `Token $ { context.state.token }`,
        }
      })
      .then(res =>
        context.commit('GET_ARTICLES', res.data)
      )
      .catch(err => console.log(err))
    },
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
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    login({ commit }, payload) {
      const username = payload.username
      const password = payload.password
      console.log(username)

      axios({
        method: 'POST',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((res) => {
          commit('SAVE_TOKEN', res.data.key)
          console.log(username)
        })
      .catch((err) => console.log(err))
    }
  },
  modules: {
  }
})
