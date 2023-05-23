<template>
<div>
    <h2>상세 상품 정보</h2>
    <div v-if="product">
    <h3>{{ product.fin_prdt_nm }}</h3>
    <!-- 상세 정보 표시 -->
    </div>
    <div v-else>
    <p>상품을 찾을 수 없습니다.</p>
    </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ProductsDetailView',
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
        .get(`/products/deposit-products/${fin_prdt_cd}/`)
        .then((res) => {
            this.product = res.data;
        })
        .catch((err) => {
          console.error(err);
          });
        },
    },
};
</script>
