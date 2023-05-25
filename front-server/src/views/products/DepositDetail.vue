<template>
<div class="deposit-pd">
    <div class="container">
    <div v-if="product">
      <h3 class="header d-flex justify-content-center text-center mt-4">상품명: {{ product.fin_prdt_nm }}</h3>
      <hr>
      <p>은행: {{ product.kor_co_nm }}</p>
      <hr>
      <p>상세 내용: {{ product.etc_note }}</p>
      <hr>
      <p>우대조건: {{ product.spcl_cnd }}</p>
      <hr>
      <ul>
        <li v-for="option in product.options" :key="option.id">
          <p>저축 기간: {{ option.save_trm }}개월</p>
          <p>저축 금리 유형 명: {{ option.intr_rate_type_nm }}</p>
          <p>적립 유형 명: {{ option.rsrv_type_nm }}</p>
          <p>저축 금리: {{ option.intr_rate }}</p>
          <p>최대 우대 금리: {{ option.intr_rate2 }}</p>
          <hr>
        </li>
      </ul>
      <SaveDepositView :fin_prdt_cd="product.fin_prdt_cd" />
    </div>
    <div v-else>
      <p>로딩 중...</p>
    </div>
  </div>
</div>

</template>

  
<script>
import SaveDepositView from '@/views/products/SaveDeposit.vue'

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DepositDetailView',
  components: {
    SaveDepositView,
  },
  data() {
    return {
    product: null,
    fin_prdt_cd: null,
    }
  },
  created() {
    this.getDepositDetail()
  },
  methods: {
    getDepositDetail() {
    const fin_prdt_cd = this.$route.params.fin_prdt_cd
    if (!fin_prdt_cd) {
        console.error('Invalid product ID')
        return
    }
    axios({
      method: 'GET',
      url: `${API_URL}/products/deposit-products/${fin_prdt_cd}/`,
      })
      .then((res) => {
        console.log(res)
        if (res.data) {
            this.product = res.data
        } else {
            console.error('No data received from the API')
        }
        })
      .catch((err) => {
        console.error(err)
        })
    },
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');
.deposit-pd {
  font-family: 'Nanum Gothic', sans-serif;
}
</style>