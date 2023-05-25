<template>
<div>
  <div class="container">
    <h1>회원가입</h1>
    <form @submit.prevent="signUp">
      <div class="mb-3">
        <label for="username" class="form-label">username : </label>
        <input type="text" class="form-control" id="username" v-model="username">
      </div>
      <div class="mb-3">
        <label for="password1" class="form-label"> password : </label>
        <input type="password" class="form-control" id="password1" v-model="password1">
      </div>
      <div class="mb-3">
        <label for="password2" class="form-label"> password confirmation : </label>
        <input type="password" class="form-control" id="password2" v-model="password2">
      </div>
      <button type="submit" class="btn btn-primary" value="SignUp">회원가입</button>
    </form>
  </div>
</div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }

      this.$store.dispatch('signUp', payload)

    }
  }
}
</script>
