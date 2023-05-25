<template>
  <div>
    <h1>{{ userData.username }}의 프로필</h1>
    <p>입출금 상품: {{ userData.deposit_fin_prdt_nm }}</p>
    <p>적금 상품: {{ userData.saving_fin_prdt_nm }}</p>
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

<style>

</style>
