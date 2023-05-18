<template>
  <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="login">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="logIn">
    </form>
      <div>
        금상 회원이 아니신가요?
        <router-link :to="{ name: 'SignUpView'}">회원가입하러 가기</router-link>
          <!-- <router-view/> -->
      </div>
  </div>
  
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)

    }
  }
}
</script>
