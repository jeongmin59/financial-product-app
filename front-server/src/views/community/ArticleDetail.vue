<template>
  <div>
    <h2>상세 정보</h2>
    <div v-if="!isEditing">
      <p>글 번호 : {{ article?.id }}</p>
      <p>작성자 : {{ article?.user }} </p>
      <p>{{ article?.category }} </p>
      <p>제목 : {{ article?.title }}</p>
      <p>내용 : {{ article?.content }}</p>
      <button @click="editArticle">수정</button>
      <button @click="deleteArticle">삭제</button>
      <CommentListView v-if="article && article.comment_set" 
      :comments="article.comment_set" />
    </div>

    <!-- 수정버튼을 누르게 되면 -->
    <div v-if="isEditing">
      <label for="title">제목 : </label>
      <input v-model="article.title" type="text" placeholder="제목" /><br>
      <label for="content">내용 : </label>
      <textarea v-model="article.content" placeholder="내용"></textarea><br>
      <label for="category">카테고리</label>
      <select v-model="article.category" placeholder="카테고리">
        <option value="예금">예금</option>
        <option value="적금">적금</option>
        <option value="기타">기타</option>
      </select><br>
      <button @click="updateArticle">수정 완료</button>
    </div>
    <div v-if="isUpdated">
      수정된 글입니다.
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommentListView from '@/components/community/CommentList.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetailView',
  components: {
    CommentListView,
  },
  data() {
    return {
      article: null,
      isEditing: false,
      isUpdated: false
    }
  },
  created() {
    this.getArticleDetail()

  },
  methods: {
    // 상세 게시글 가져오기
    getArticleDetail() {
      axios({
        method: 'GET',
        url: `${API_URL}/articles/${ this.$route.params.id }/`,
      })
      .then((res) => {
        console.log(res)
        this.article = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },

    // 게시글 수정 메서드
    editArticle() {
      this.isEditing = true
    },
    updateArticle() {
      axios({
        method: 'PUT',
        url: `${API_URL}/articles/${ this.$route.params.id }/`,
        data: {
          title: this.article.title,
          content: this.article.content,
          category: this.article.category,
        }
      })
      .then((res) => {
        console.log(res)
        this.isEditing = false
        this.isUpdated = true
        // this.getArticleDetail()
      })
      .catch((err) => {
        console.log(err)
      })
    },

    // 게시글 삭제 메서드
    deleteArticle() {
      axios({
        method: 'delete',
        url: `${API_URL}/articles/${this.article.id}/`
      })
      .then((res) => {
        console.log(res)
        // 삭제 성공 후 처리
        alert('삭제되었습니다.') // 삭제 성공 시 팝업 메시지
        this.$router.push('/community') // Community 페이지로 이동
      })
      .catch((err) => {
        console.log(err)
      })
    }

  }
}
</script>
