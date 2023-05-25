<template>
<div id="app">
  <nav class="navbar navbar-expand-lg bg-light">
    <!-- bg-light -->
    <div class="container-fluid">
      <a class="navbar-brand" href="/">
        <img src="@/assets/logo.png" alt="logo" width="150" height="50">
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse d-flex justify-content-between" id="navbarNavAltMarkup">
        <ul class="navbar-nav fs-5">
          <li class="nav-item">
            <a class="nav-link" href="/">홈</a>
            <!-- 로고 누르면 홈으로 가게 해도 될 듯 -->
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/products">금융 상품</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/recommend-products">상품 추천</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/community">게시판</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/Exchange">환율 계산</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/KakaoMap">은행 찾기</a>
          </li>
        </ul>
        <ul class="navbar-nav fs-5">
          <li class="nav-item">
            <a class="nav-link" v-if="isLoggedIn" href="/logout" @click="logout">로그아웃</a>
            <a class="nav-link" v-else href="/login">로그인</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" v-if="isLoggedIn" href="/profile">프로필</a>
            <a class="nav-link" v-else href="/signup">회원가입</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
<!-- 라우터 링크 하지 말까 고민 중 -->
  <!-- <div class="navbar-nav">
    <a class="nav-link"><router-link :to="{ name: 'HomeView' }">Home</router-link></a>
    <a class="nav-link"><router-link :to="{ name: 'ProductsView' }">Products</router-link></a>
    <a class="nav-link"><router-link :to="{ name: 'CommunityView' }">Community</router-link></a>
    <a class="nav-link"><router-link :to="{ name: 'ExchangeView' }">Exchange</router-link></a>
    <a class="nav-link" href="#">Kakaomap</a>
  </div> -->
</div>
</template>

<script>
export default {
  computed: {
    isLoggedIn() {
      // 토큰의 존재 여부에 따라 true 또는 false를 반환하는 computed 속성
      return this.$store.state.token ? true : false;
    },
  },
  methods: {
    logout() {
      // 로그아웃 버튼을 클릭하면 실행될 메서드
      // 토큰을 null로 설정하거나 삭제하는 등의 작업을 수행합니다.
      this.$store.commit('SAVE_TOKEN', null); // 예시: Vuex를 사용하여 토큰을 관리하는 경우
      // 다른 로그아웃 관련 작업을 수행할 수도 있습니다.
      // 예: 로컬 스토리지에서 토큰 삭제 등
      
      // 로그아웃 후에 홈페이지 또는 로그인 페이지 등으로 이동할 수 있습니다.
      // 예: 홈페이지로 이동
      this.$router.push('/');
    }
  }
};
</script>

<style>
/* .navbar {
  background-color: #DCEBFF;
} */
</style>
