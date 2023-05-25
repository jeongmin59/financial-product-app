<template>
  <!-- 목록 안에 어떤 내용이 보일지에 대한 컴포넌트 -->
  <div class="article-list-item">
    <div class="container">
      <div class="article-info">
        <h5 class="id">{{ article.id }}</h5>
        <p class="category">{{ article.category }}</p>
      </div>
      <router-link :to="{ name: 'ArticleDetailView', params: { id: article.id }}">
        <p class="title">{{ article.title }}</p>
      </router-link>
      <div class="additional-info">
        <div class="info-group">
          <p class="comment-count">댓글 수: {{ article.comment_count }}</p>
          <p class="username">작성자: {{ article.username }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItemView',
  props: {
    article: Object,
  }
}
</script>

<style scoped>
.container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
}

.article-info {
  display: flex;
}
.id,
.category {
  margin-right: 50px;
}

.title {
  flex-grow: 1;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.additional-info {
  display: flex;
  align-items: center;
}

.info-group {
  display: flex;
  align-items: center;
}

.comment-count,
.username {
  margin-right: 10px;
  margin-left: 40px;
}
</style>
