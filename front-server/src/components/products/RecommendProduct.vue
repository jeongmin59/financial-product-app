Copy code
<template>
<div class="recommend-product">
  <div class="container">
    <h1 class="header d-flex justify-content-center text-center mt-4">상품 추천</h1>
    <div class="form-group">
      <h4>
        <label for="productType">상품 종류</label>
      </h4>
      <select id="productType" class="form-control" v-model="productType">
        <option value="예금">예금</option>
        <option value="적금">적금</option>
      </select>
    </div>
    <div class="form-group">
      <h4>
        <label for="amount">금액</label>
      </h4>
      <input type="number" id="amount" class="form-control" v-model.number="amount" />
    </div>
    <div class="form-group">
      <h4>
        <label for="duration">기간</label>
      </h4>
      <select name="duration" class="form-control" v-model="duration">
        <option value="6">6</option>
        <option value="12">12</option>
        <option value="24">24</option>
        <option value="30">30</option>
      </select>
    </div>
    <div class="form-group">
      <h4>
        <label for="preferredBanks">선호하는 은행</label>
      </h4>
      <div class="checkbox-group">
        <div v-for="bank in banks" :key="bank" class="form-check form-check-inline">
          <input
            type="checkbox"
            :id="bank"
            :value="bank"
            class="form-check-input"
            v-model="preferredBanks[bank]"
          />
          <label :for="bank" class="form-check-label">{{ getFormattedBankName(bank) }}</label>
        </div>
      </div>
    </div>
    <div class="form-group">
      <div class="form-check">
        <input type="checkbox" id="preferredCondition" class="form-check-input" v-model="preferredCondition" />
        <label for="preferredCondition" class="form-check-label">우대 조건에 따른 이율을 적용합니다.</label>
      </div>
    </div>
    <button @click="recommendProducts" class="btn btn-primary">상품 추천 받기</button>
    <div v-if="recommendationList.length" class="recommendation-list">
      <h3>추천 상품 리스트</h3>
      <ul class="list-group">
        <li v-for="(product, index) in recommendationList" :key="index" class="list-group-item">
          <p>은행: {{ product.은행 }}</p>
          <p>상품: {{ product.상품 }}</p>
          <p>이율: {{ product.이율 }}</p>
          <p>예상금액: {{ calculateExpectedAmount(product) }}원</p>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>추천 상품이 없습니다.</p>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'RecommendProductView',
  data() {
    return {
      productType: '예금',
      amount: 0,
      duration: 0,
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
      preferredBanks: {},
      preferredCondition: false,
      recommendationList: [],
    }
  },
  methods: {
    recommendProducts() {
      const selectedBanks = Object.keys(this.preferredBanks).filter(
        (bank) => this.preferredBanks[bank]
      )
      axios
        .post(`${API_URL}/products/recommend-products/`, {
          product_type: this.productType,
          amount: this.amount,
          duration: this.duration,
          preferred_banks: selectedBanks,
          preferred_condition: this.preferredCondition,
        })
        .then((res) => {
          this.recommendationList = res.data['추천 상품']
        })
        .catch((err) => {
          console.error(err)
        })
    },
    calculateExpectedAmount(product) {
      if (this.productType === '예금') {
        // 예금 계산식
        return (
          this.amount +
          (this.amount * product.이율 * this.duration) / 100
        )
      } else if (this.productType === '적금') {
        // 적금 계산식
        return (
          this.amount +
          (this.amount * product.이율 * this.duration * 12) / 100
        )
      }
      return 0 // 기타 경우에는 0으로 처리하거나 적절한 값으로 수정하세요.
    },
    getFormattedBankName(bank) {
      const formattedNames = {
        '농협은행주식회사': '농협은행',
        '주식회사 카카오뱅크': '카카오뱅크',
        '주식회사 케이뱅크': '케이뱅크',
        '토스뱅크 주식회사': '토스뱅크',
      }
      return formattedNames[bank] || bank
    },
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');
.recommend-product {
  font-family: 'Nanum Gothic', sans-serif;
}
.checkbox-group .form-check {
  margin-right: 10px;
}

.recommendation-list {
  margin-top: 20px;
}
.form-check {
  border: none;
}
h4 {
  margin-top: 20px;
}

div p {
  margin-top: 20px;
}

</style>