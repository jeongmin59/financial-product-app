<template>
<div class="profile">
  <div class="container">
    <h1 class="header d-flex justify-content-center text-center mt-4">{{ userData.username }}의 프로필</h1>
    <div class="product d-flex justify-content-center text-center">저장한 예금 상품: {{ userData.deposit_fin_prdt_nm }}</div>
    <div class="product d-flex justify-content-center text-center">저장한 적금 상품: {{ userData.saving_fin_prdt_nm }}</div>
  </div>
</div>
</template>

<script>
import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  data() {
    return {
      userData: {},
    };
  },
  mounted() {
    this.fetchProfileData();
  },
  methods: {
    fetchProfileData() {
      axios({
        method: 'GET',
        url: `${API_URL}/accounts/profile/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        })
        .then(res => {
          this.userData = res.data;
        })
        .catch(err => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');
.profile {
  font-family: 'Nanum Gothic', sans-serif;
}

.product {
  margin-top: 20px;
}
</style>
