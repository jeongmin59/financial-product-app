<template>
<div>
  <h3 v-if="product">상품명: {{ product.fin_prdt_nm }}</h3>
  <br>
  <p v-if="product">은행: {{ product.kor_co_nm }}</p>
  <br>
  <p v-if="product">상세 내용: {{ product.etc_note }}</p>
  <br>
  <p v-if="product">우대조건: {{ product.spcl_cnd }}</p>
  <br>
  <ul v-if="product">
    <li v-for="option in product.options" 
    :key="option.id">
      저축 기간 : {{ option.save_trm }}개월
      <br>
      저축 금리 유형 명 : {{ option.intr_rate_type_nm }}
      <br>
      적립 유형 명 : {{ option.rsrv_type_nm }}
      <br>
      저축 금리 : {{ option.intr_rate }}
      <br>
      최대 우대 금리 : {{ option.intr_rate2 }}
      <br>
      <br>
    </li>
  </ul>
  <SaveDepositView v-if="product" :fin_prdt_cd="product.fin_prdt_cd"/>
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

</style>