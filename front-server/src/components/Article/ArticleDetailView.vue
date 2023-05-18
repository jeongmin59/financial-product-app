<template>
  <div>
    <h1>상세 조회</h1>
    <h5>글 번호: {{ article?.id }}</h5>
    <p>제목: {{ article?.title }}</p>
    <p>내용: {{ article?.content }}</p>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetail',
  props: {
    articles: null
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'GET',
        url: `${API_URL}/articles/${this.$route.params.id}/`,
      })
      .then((res) => {
        this.article = res.data
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style>

</style>