<template>
<!-- 댓글 목록 안 내용들 -->
  <div>
    <h5>{{ comment.id }}</h5>
    <p>{{ comment.content }}</p>
    <router-link :to="{
      name: 'CommentDetailView',
      params: { id: comment.id }}"><p>{{ comment.content }}</p>
    </router-link>
    <p>작성자: {{ comment.username }}</p>
    <!-- <p>좋아요 수: {{ 바꿔  }} </p> -->
    <br>
  </div>
</template>

<script>
export default {
  name: 'CommentListItem',
  props: {
    comment: Object,
  }
}
</script>

<style>

</style>