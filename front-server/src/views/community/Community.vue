<template>
  <div class="community">
    <div class="container">
      <h1 class="header d-flex justify-content-center text-center mt-4">게시판</h1>
      <h5  class="text d-flex justify-content-center text-center mt-4">회원들 간 자유롭게 의견을 공유하는 하는 공간입니다. </h5>
      <div class="d-flex justify-content-end">
        <button class="create-button" @click="navigateToCreate">글 작성</button>

        <!-- <router-link :to="{ name: 'ArticleCreateView' }">글 작성</router-link> -->
      </div>
      <ArticleList />
    </div>
  </div>
</template>

<script>
import ArticleList from '@/views/community/ArticleList.vue'

export default {
  name: 'CommunityView',
  components: {
    ArticleList,
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 페이지입니다...')
        this.$router.push({ name: 'LogInView' })
      }
    },
    navigateToCreate() {
      this.$router.push({ name: 'ArticleCreateView' })
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');
.community {
  font-family: 'Nanum Gothic', sans-serif;
}
.create-button {
  font-size: 18px;
  color: #fff;
  background-color: #007bff;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.create-button:hover {
  background-color: #0056b3;
}
</style>