<template>
  <div id="app">
    <header-nav></header-nav>
    <router-view></router-view>
    <footer-nav></footer-nav>
  </div>
</template>


<script>
import HeaderNav from '@/components/HeaderNav.vue'
import FooterNav from '@/components/FooterNav.vue'

import { mapActions } from 'vuex'


export default {
  name: 'App',
  components: { 
    HeaderNav, FooterNav
  },
  computed: {
    ...mapActions([
      'checkLogin'
    ]),
  },
  methods: {
  getToken() {
    const token = localStorage.getItem('jwt')
    return token
  },
  setToken() {
    const token = localStorage.getItem('jwt')
    const config = {
      Authorization: `JWT ${token}`
    }
    return config
    },
  },
  created() {
    this.$store.dispatch('checkLogin', this.getToken())
  },
}
</script>

<style>

</style>
