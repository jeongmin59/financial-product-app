<template>
<div>
  <div v-if="product">
    <h5>{{ product.fin_prdt_nm }}</h5>
    <button @click="saveProduct">상품 저장</button>
  </div>
  <div v-else>
    <p>상품을 찾을 수 없습니다.</p>
  </div>
</div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'SaveDepositView',
  data() {
    return {
      product: null,
    };
  },
  mounted() {
    const fin_prdt_cd = this.$route.params.fin_prdt_cd;
    this.fetchProduct(fin_prdt_cd);
  },
  methods: {
    fetchProduct(fin_prdt_cd) {
    axios
      .get(`${API_URL}/products/deposit-products/${fin_prdt_cd}/`)
      .then((res) => {
      this.product = res.data;
      })
      .catch((err) => {
      console.error(err);
      });
    },
    saveProduct() {
    // 저장 로직 구현
      if (!this.product) {
        console.error('상품 정보가 없습니다.');
        return;
      }
      axios({
        method: 'POST',
        url: `${API_URL}/accounts/profile/`,
        data: this.product,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then((res) => {
        alert('상품이 성공적으로 저장되었습니다.')
        console.log('상품이 성공적으로 저장되었습니다.', res);
      })
      .catch((err) => {
        console.error('상품 저장에 실패했습니다.', err);
      });
    },
  },
};
</script>
