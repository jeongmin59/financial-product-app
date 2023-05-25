<template>
<!-- 댓글 목록 안 내용들 -->
  <div>
    <h5>댓글</h5>
    <div v-for="comment in comments" 
    :key="comment.id">
      <p>내용: {{ comment.content }} </p>
      <p>작성자: {{ comment.username }} </p>
      <p>좋아요 수: {{ comment.like_count }} </p>
      <button @click="toggleLike(comment)">
        {{ comment.liked_by_user ? '좋아요 취소' : '좋아요' }}
        </button>
      <br>
    </div>
  </div>
</template>
  
<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentListItemView',
  props: {
    comments: { 
      type: Array,
      required: true,
    }
  },
  methods: {
    toggleLike(comment) {
      const articleId = comment.article;
      const commentId = comment.id;

      axios({
        method: 'POST',
        url: `${API_URL}/articles/${articleId}/${commentId}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res => {
        if (res.data.message === 'Comment liked successfully.') {
          comment.liked_by_user = true; // 좋아요 상태로 업데이트
          alert('이 댓글을 좋아합니다.');
        } else if (res.data.message === 'Comment unliked successfully.') {
          comment.liked_by_user = false; // 좋아요 취소 상태로 업데이트
          alert('이 댓글의 좋아요를 취소하였습니다.');
        }
        window.location.reload();
        console.log(res.data.message);
        comment.like_count = res.data.like_count
      })
      .catch(err => {
        console.error(err);
      });
    }
  }

}
</script>

<style>

</style>