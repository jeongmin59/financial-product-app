<template>
<!-- 댓글 목록 출력되는 컴포넌트 -->
  <div class="comment-list">
    <h3>댓글 목록</h3>
    <router-link :to="{ name: 'CommentCreateView' }">[댓글 작성]</router-link>
    <CommentListItem 
    v-for="comment in comments" :key="comment.id" :comment="comment"
    />
    <hr>
  </div>
</template>

<script>
import CommentListItem from '@/components/community/CommentListItem'

export default {
  name: 'CommentList',
  components: {
    CommentListItem
  },
  computed: {
    comments() {
        return this.$store.state.comments
    }
  },
}
</script>

<style>

</style>