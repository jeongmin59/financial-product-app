<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'ProductsView' }">Products</router-link> | 
      <router-link :to="{ name: 'CommunityView' }">Community</router-link> | 
      <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link> | 
      <router-link :to="{ name: 'LogInView' }">LogInPage</router-link>
    </nav>
  </div>
</template>

<style>

</style>
