<template>
<!-- 목록 안에 어떤 내용이 보일지에 대한 컴포넌트 -->
  <div>
    <h5>{{ article.id }}</h5>
    <p>{{ article.category }}</p>
    <router-link :to="{
        name: 'ArticleDetailView',
        params: { id: article.id }}"><p>{{ article.title }}</p>
    </router-link>
    <p>작성자: {{ article.username }}</p>
    <p>댓글 수: {{ article.comment_count }} </p>
    <br>
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

<style>

</style>
