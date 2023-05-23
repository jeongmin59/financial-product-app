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
