<template>
  <!-- 댓글 생성 -->
  <div>
    <h2>댓글 작성</h2>
    <form @submit.prevent="createComment">
      <label for="content">내용 : </label>
      <textarea id="content" cols="20" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentCreateView',
  data() {
    return {
      content: null,
    }
  },
  
  methods: {
    createComment() {
      const content = this.content

      if (!content) {
        alert('내용을 입력해주세요')
      }
      axios({
        method: 'POST',
        url: `${API_URL}/articles/${this.$route.params.id}/comments/`,
        data: { content, },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.$router.push({ name: 'ArticleDetailView' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }

}
</script>

<style>

</style>