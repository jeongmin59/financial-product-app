<template>
<div>
  <button @click="saveDeposit">상품 저장</button>
    <!-- <h3>SaveDepositView Component</h3>
    <p>Product ID: {{ fin_prdt_cd }}</p> -->
    <!-- 상품 정보를 표시하는 내용 -->
</div>
</template>

<script>
import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000';

export default {
  name: 'SaveDepositView',
  // props: {
  //     fin_prdt_cd: {
  //     type: String,
  //     required: true,
  //   },
  // },
  
  data() {
    return {
      product: null,
    };
  },
  mounted() {
    this.fetchProductData();
  },
  methods: {
    fetchProductData() {
      axios
        .get(`${API_URL}/products/deposit-products/${this.fin_prdt_cd}/`)
        .then((res) => {
          console.log(res);
          if (res.data) {
            this.product = res.data;
            this.$emit('product-updated', this.product); // 이벤트를 발생시켜 상위 컴포넌트에 상품 데이터 전달
          } else {
            console.error('No data received from the API');
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>

<style>

</style>
