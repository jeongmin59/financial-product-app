<template>
<div>
    <h2>전체 상품 목록</h2>
    <ul>
    <li v-for="product in products" :key="product.fin_prdt_cd">
        {{ product.fin_prdt_nm }}
    </li>
    </ul>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ProductsListView',
  data() {
    return {
    products: [],
    };
  },
  mounted() {
    this.fetchProducts();
  },
  methods: {
    fetchProducts() {
    axios
      .get('/products/deposit-products/')
      .then((res) => {
        this.products = res.data;
      })
      .catch((err) => {
        console.error(err);
      });
    },
  },
};
</script>
  