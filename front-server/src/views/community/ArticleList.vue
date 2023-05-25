<template>
<!-- 목록 출력되는 컴포넌트 -->
  <div class="article-list">
    <h3>Article List</h3>
    <ArticleListItemView 
    v-for="article in articles" :key="article.id" :article="article"
    />
  </div>
</template>

<script>
import ArticleListItemView from '@/views/community/ArticleListItem'

export default {
  name: 'ArticleListView',
  components: {
    ArticleListItemView,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  }
}
</script>

<style>
.article-list {
  text-align: start;
}
</style>
