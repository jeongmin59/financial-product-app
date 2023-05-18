<template>
  <div class="header">
    <nav class="navbar navbar-expand-lg bg-light bg-white">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">금상</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
          aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav mx-auto">
            <!-- 카테고리 -->
            <li class="nav-item">
              <router-link class="nav-link text-center" aria-current="page" to="/" style="color:black">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link text-center" to="/interest" style="color:black">금리 비교</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link text-center" to="/exchange_info" style="color:black">환율 정보</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link text-center" to="/nearby_bank" style="color:black">근처 은행 찾기</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link text-center" to="/community" style="color:black">게시판</router-link>
            </li>
            <!-- 로그인 -->
            <li class="nav-item">
              <router-link v-if="!isLoggedIn" class="nav-link" :to="{ name: 'LogInView' }" style="color:black">로그인</router-link>
            </li>
            <!-- 로그아웃 -->
            <li class="nav-item">
              <router-link v-if="isLoggedIn" @click.native="logout" class="nav-link" to="/" style="color:black">로그아웃</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'HeaderNavbar',
  methods: {
    logout() {
      this.$store.dispatch('logout')
    },
    // getToken() {
    //   const token = localStorage.getItem('jwt')
    //   return token
    // },
    // setToken() {
    //   const token = localStorage.getItem('jwt')
    //   const config = {
    //     Authorization: `JWT ${token}`
    //   }
    //   return config
    // },
  },
  computed: {
    ...mapActions([
      'checkLogin'
    ]),
    ...mapGetters([
      'isLogin'
    ])
  },
  created() {
    this.$store.dispatch('checkLogin', this.getToken())
  }
}
</script>

<style scoped>

.nav-link{
  padding: 0; /* 패딩 제거 */
  margin: 0 40px; /* 좌우 여백 추가 */
}

.navbar-brand {
  padding: 5px;
}

</style>