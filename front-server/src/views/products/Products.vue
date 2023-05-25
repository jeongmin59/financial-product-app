<template>
<div class="products">
  <div class="container">
    <h1 class="header d-flex justify-content-center text-center mt-4">금융 상품 조회</h1>
    <div class="row row-cols-1 row-cols-md-2 mt-5">
      <div class="col">
        <div class="card deposit-card" @click="goToDepositList">
          <div class="card-body">
            <h3 class="card-title">예금 조회
              <h5 class="card-text mt-4">지금 바로 예금 상품을 확인하세요!</h5>
            </h3>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card saving-card" @click="goToSavingList">
          <div class="card-body">
            <h3 class="card-title">적금 조회
              <h5 class="card-text mt-4">지금 바로 적금 상품을 확인하세요!</h5>
            </h3>
            
          </div>
        </div>
      </div>
    </div>
  </div>

</div>
</template>

<script>
import DepositListView from '@/views/products/DepositList.vue'
import SavingListView from '@/components/products/SavingList.vue'

export default {
  name: 'ProductsView',
  components: {
    DepositListView,
    SavingListView,
  },
  methods: {
    goToDepositList() {
      this.$router.push('/products/deposit-products/');
    },
    goToSavingList() {
      this.$router.push('/products/saving-products/');
    },
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');
.products {
  font-family: 'Nanum Gothic', sans-serif;
}
.card {
  cursor: pointer;
  height: 200px;
}
.card-body {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.deposit-card {
  background-color: #008ad2;
  border-radius: 0 16px 0 16px;
  border: none;
}
.saving-card {
  background-color: #046fd9;
  border-radius: 0 16px 0 16px;
  border: none;
}
.card-title {
  font-weight: bold;
  /* text-align: left; */
}
.card-body {
 margin: 10px 10px;
 color: white;
}
</style>
