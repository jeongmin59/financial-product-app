<template>
<div>
  <h2>적금 상품 조회</h2>
  <ul>
  <SavingListItemView
      v-for="product in products"
      :key="product.fin_prdt_cd"
      :product="product"
  />
  </ul>
</div>
</template>

<script>
import axios from 'axios'
import SavingListItemView from '@/components/products/SavingListItem.vue'

const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'SavingListView',
  components: {
      SavingListItemView,
  },
  data() {
    return {
    products: [], // 상품 데이터를 저장할 배열
    }
  },
  created() {
    this.fetchProducts() // 생성될 때 상품 데이터를 가져오도록 호출
  },
  methods: {
    fetchProducts() {
    // axios를 사용하여 상품 데이터를 가져옴
    axios({
      method: 'GET',
      url: `${API_URL}/products/saving-products/`,
    })
      .then((response) => {
        this.products = response.data // 상품 데이터를 저장
      })
      .catch((error) => {
        console.error(error)
      })
    },
  },
}
</script>