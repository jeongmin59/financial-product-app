<template>
<div class="saving-list">
  <div class="container">
    <h1 class="header d-flex justify-content-center text-center mt-4">적금 상품 조회</h1>
    <div class="form-check mt-4">
      <label v-for="bank in banks" :key="bank">
        <input type="checkbox" :value="bank" v-model="selectedBanks" @change="filterProductsByBanks">
        {{ getFormattedBankName(bank) }}
      </label>
    </div>
    <div class="container list-container">
      <div class="product-list">
        <SavingListItemView
          v-for="product in filteredProducts"
          :key="product.fin_prdt_cd"
          :product="product"
        />
      </div>
    </div>

  </div>

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
      filteredProducts: [], // 선택한 은행에 해당하는 상품 데이터를 저장할 배열
      selectedBanks: [], // 선택한 은행들을 저장할 배열
      banks: [
        '경남은행',
        '광주은행',
        '국민은행',
        '농협은행주식회사',
        '부산은행',
        '수협은행',
        '신한은행',
        '우리은행',
        '전북은행',
        '제주은행',
        '중소기업은행',
        '주식회사 카카오뱅크',
        '주식회사 케이뱅크',
        '토스뱅크 주식회사',
        '한국산업은행',
        '한국스탠다드차타드은행',
      ],
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
          this.filterProductsByBanks() // 은행 선택에 따라 상품 필터링
        })
        .catch((error) => {
          console.error(error)
        })
    },
    filterProductsByBanks() {
      if (this.selectedBanks.length > 0) {
        this.filteredProducts = this.products.filter((product) => {
          return this.selectedBanks.includes(product.kor_co_nm)
        })
      } else {
        this.filteredProducts = this.products // 선택한 은행이 없을 경우 모든 상품 출력
      }
    },
    getFormattedBankName(bank) {
      const formattedNames = {
        '농협은행주식회사': '농협은행',
        '주식회사 카카오뱅크': '카카오뱅크',
        '주식회사 케이뱅크': '케이뱅크',
        '토스뱅크 주식회사': '토스뱅크',
      };
      return formattedNames[bank] || bank;
    },
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');
.saving-list {
  font-family: 'Nanum Gothic', sans-serif;
}
.form-check {
  display: flex;
  flex-wrap: wrap;
  border: 1px solid black;
  padding: 15px;
}
.form-check label {
  margin-right: 15px;
}
.list-container {
  margin-top: 30px; /* form-check과 ul 사이에 마진을 추가 */
}
.product-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  grid-gap: 20px;
}
</style>