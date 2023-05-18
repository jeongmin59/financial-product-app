<template>
  <div>
    <h1>Community Page</h1>
    <h3>다양한 정보들을 공유해주세요!</h3>
    <router-link :to="{ name: 'article_create' }">
      [CREATE]
    </router-link>
    <hr>
    <router-view></router-view>
    <ArticleList />
  </div>
</template>

<script>
import ArticleList from '@/views/Community/ArticleListView.vue'

export default {
  name: 'CommunityView',
  components: {
    ArticleList,
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LogInView'})
      }
      
    }
  }

}
</script>

<style>

</style>