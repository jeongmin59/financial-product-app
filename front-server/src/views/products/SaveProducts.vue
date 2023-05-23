<template>
<div>
    <h2>상품 저장</h2>
    <div v-if="product">
    <h3>{{ product.fin_prdt_nm }}</h3>
    <button @click="saveProduct">상품 저장</button>
    </div>
    <div v-else>
    <p>상품을 찾을 수 없습니다.</p>
    </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
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
        .get(`/api/deposit-products/${fin_prdt_cd}/`)
        .then((response) => {
        this.product = response.data;
        })
        .catch((error) => {
        console.error(error);
        });
    },
    saveProduct() {
    // 저장 로직 구현
    },
},
};
</script>
