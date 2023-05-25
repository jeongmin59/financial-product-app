<!-- ArticleListView.vue -->
<template>
  <div>
    <div class="category-list btn-group" role="group" aria-label="Basic outlined example">
      <button type="button" class="btn btn-outline-primary" @click="selectCategory(null)">전체</button>
      <button type="button" class="btn btn-outline-primary" @click="selectCategory('예금')">예금</button>
      <button type="button" class="btn btn-outline-primary" @click="selectCategory('적금')">적금</button>
      <button type="button" class="btn btn-outline-primary" @click="selectCategory('기타')">기타</button>
    </div>
    <div class="article-list">
      <h3 class="header d-flex justify-content-center text-center mt-2 mb-5">게시글 목록</h3>
      <ArticleListItemView
        v-for="article in filteredArticles"
        :key="article.id"
        :article="article"
        :selectedCategory="selectedCategory"
      />
    </div>
  </div>
</template>

<script>
import ArticleListItemView from '@/views/community/ArticleListItem'
import { mapState, mapMutations } from 'vuex'

export default {
  name: 'ArticleListView',
  components: {
    ArticleListItemView,
  },
  computed: {
    ...mapState(['articles', 'selectedCategory']),
    filteredArticles() {
      if (this.selectedCategory) {
        return this.articles.filter(article => article.category === this.selectedCategory)
      } else {
        return this.articles // 선택한 카테고리가 없을 경우 전체 게시글 반환
      }
    },
  },
  methods: {
    ...mapMutations(['SET_SELECTED_CATEGORY']),
    selectCategory(category) {
      this.SET_SELECTED_CATEGORY(category)
    },
  },
}
</script>

<style>
.category-list {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.category-list button {
  margin-right: 10px;
}

.article-list {
  text-align: start;
}
</style>
