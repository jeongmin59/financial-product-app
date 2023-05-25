<template>
  <div>
    <button @click="saveDeposit">상품 저장</button>
  </div>
</template>

<script>
import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000';

export default {
  name: 'SaveDepositView',
  props: ['fin_prdt_cd'],
  data() {
    return {
      product: null,
      deposit_fin_prdt_nm: '', // deposit_fin_prdt_nm 데이터
      saving_fin_prdt_nm: '', // saving_fin_prdt_nm 데이터
    };
  },
  created() {
    this.getDepositDetail();
  },
  methods: {
    saveDeposit() {
      const user = this.$store.getters['user/getUsername']; // Vuex 스토어에서 user 정보 가져오기

      const data = {
        username: user, // 사용자 이름 데이터
        deposit_fin_prdt_nm: this.deposit_fin_prdt_nm, // deposit_fin_prdt_nm 데이터
        saving_fin_prdt_nm: this.saving_fin_prdt_nm, // saving_fin_prdt_nm 데이터
      };

      axios
        .post(`${API_URL}/products/deposit-products/${this.fin_prdt_cd}`, data) // fin_prdt_cd 수정
        .then((res) => {
          // 저장이 완료되었을 때 수행할 동작
          alert('상품이 성공적으로 저장되었습니다.');
          console.log('상품이 성공적으로 저장되었습니다.', res);
          this.$router.push('/profile'); // Profile 페이지로 네비게이션
        })
        .catch((err) => {
          console.error('상품 저장에 실패했습니다.', err);
        });
    },
    getDepositDetail() {
      // 상품 상세 정보를 가져오는 코드
    },
  },
};
</script>

<style>

</style>
