<template>
<!-- 댓글 목록 안 내용들 -->
  <div>
    <h3>댓글</h3>
    <div v-if="!isEditing">
      <h5>{{ comment.id }}</h5>
      <p>{{ comment.content }}</p>
      <p>작성자: {{ comment.username }}</p>
    <!-- <p>좋아요 수: {{ 바꿔  }} </p> -->
      <button @click="toggleEditMode">수정</button>
      <button @click="deleteArticle">삭제</button>
    </div>
  </div>
</template>
  
<script>
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentListItemView',
  props: {
    comment: Object,
  },
  data() {
    return {
      isEditMode: false, // 수정 모드인지 여부를 저장하는 상태
      updatedCommentText: '', // 수정된 댓글 내용을 저장하는 상태
    };
  },

  methods: {
    toggleEditMode() {
      this.isEditMode = !this.isEditMode;

      // 수정 모드가 활성화되면, 수정된 댓글 내용을 초기화합니다.
      if (this.isEditMode) {
        this.updatedCommentText = this.comment.text;
      }
    },
    saveUpdatedComment() {
      const updatedCommentData = {
        id: this.comment.id,
        text: this.updatedCommentText,
      };
      // 서버로 댓글 수정 요청을 보냅니다.
      this.updateComment(updatedCommentData)
        .then(() => {
          // 댓글 수정이 성공하면, 필요한 동작을 수행합니다. 예: 수정된 댓글을 화면에 반영하기
          this.isEditMode = false;
        })
        .catch((error) => {
          // 댓글 수정 실패 시, 에러 처리를 합니다.
          console.error('댓글 수정 실패:', error);
        });
    },
    deleteComment() {
      const commentId = this.comment.id;
      // 서버로 댓글 삭제 요청을 보냅니다.
      this.deleteComment(commentId)
        .then(() => {
          // 댓글 삭제가 성공하면, 필요한 동작을 수행합니다. 예: 삭제된 댓글을 화면에서 제거하기
        })
        .catch((error) => {
          // 댓글 삭제 실패 시, 에러 처리를 합니다.
          console.error('댓글 삭제 실패:', error);
        });
    },
  },


}
</script>

<style>

</style>