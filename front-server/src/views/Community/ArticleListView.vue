<template>
  <div class="article-list">
    <h5>목록 출력</h5>
    <ArticleDetailView
      v-for="article in articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script>
import ArticleDetailView from '@/components/Article/ArticleDetailView.vue'

export default {
  name: 'ArticleList',
  components: {
    ArticleDetailView,
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