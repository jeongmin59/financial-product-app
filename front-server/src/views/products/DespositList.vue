<template>
  <div>
    <h2>전체 예금 조회</h2>
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
  name: 'DespositListView',
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
      