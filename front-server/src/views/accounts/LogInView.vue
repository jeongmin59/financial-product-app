<template>
<div>
  <div class="container">
    <h1>로그인</h1>
    <form @submit.prevent="login">
      <div class="mb-3">
        <label for="username" class="form-label">username : </label>
        <input type="text" class="form-control" id="username" v-model="username">
      </div>
      <div class="mb-3">
        <label for="password" class="form-label"> password : </label>
        <input type="password" class="form-control" id="password" v-model="password"><br>
      </div>
      <button type="submit" class="btn btn-primary" value="logIn">로그인</button>
    </form>
  </div>
<!-- 회원이 아니라면 회원가입 페이지 만들기 -->
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
