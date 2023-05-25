<template>
 <div class="app">
  <header-nav></header-nav>
  <router-view></router-view>
  <footer-nav></footer-nav>
 </div>
</template>

<script>
import HeaderNav from './components/HeaderNav.vue';
import FooterNav from './components/FooterNav.vue';

export default {
  name: 'App',
  components: { 
    HeaderNav,
    FooterNav,
  },
};
</script>

<style>
/* @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');
#app {
  font-family: 'Nanum Gothic', sans-serif;
} */
</style>
