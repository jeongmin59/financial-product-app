<template>
    <div>
      <h2>상품 추천</h2>
      <div>
        <label for="productType">상품 종류</label>
        <select id="productType" v-model="productType">
          <option value="예금">예금</option>
          <option value="적금">적금</option>
        </select>
      </div>
      <div>
        <label for="amount">금액</label>
        <input type="number" id="amount" v-model.number="amount" />
      </div>
      <div>
        <label for="duration">기간</label>
        <select name="duration" v-model="duration">
          <option value="6">6</option>
          <option value="12">12</option>
          <option value="24">24</option>
          <option value="30">30</option>
        </select>
      </div>
      <div>
        <label for="preferredBanks">선호하는 은행</label>
        <select id="preferredBanks" v-model="preferredBanks" multiple>
          <option value="경남은행">경남은행</option>
          <option value="광주은행">광주은행</option>
          <option value="국민은행">국민은행</option>
          <option value="농협은행주식회사">농협은행</option>
          <option value="부산은행">부산은행</option>
          <option value="수협은행">수협은행</option>
          <option value="신한은행">신한은행</option>
          <option value="우리은행">우리은행</option>
          <option value="전북은행">전북은행</option>
          <option value="제주은행">제주은행</option>
          <option value="중소기업은행">중소기업은행</option>
          <option value="주식회사 카카오뱅크">카카오뱅크</option>
          <option value="주식회사 케이뱅크">케이뱅크</option>
          <option value="토스뱅크 주식회사">토스뱅크</option>
          <option value="한국산업은행">한국산업은행</option>
          <option value="한국스탠다드차타드은행">한국스탠다드차타드은행</option>
      </select>
      </div>
      <div>
        <label for="preferredCondition">우대 조건</label>
        <input type="checkbox" id="preferredCondition" v-model="preferredCondition" />
        <span>조건에 따른 이율을 적용합니다.</span>
      </div>
      <button @click="recommendProducts">상품 추천 받기</button>
      <div v-if="recommendationList.length">
        <h3>추천 상품 리스트</h3>
        <ul>
            <li v-for="(product, index) in recommendationList" :key="index">
            <p>은행: {{ product.은행 }}</p>
            <p>상품: {{ product.상품 }}</p>
            <p>이율: {{ product.이율 }}</p>
            <p>예상금액 : {{ calculateExpectedAmount(product) }}원 </p>
            </li>
        </ul>
      </div>
      <div v-else>
        <p>추천 상품이 없습니다.</p>
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
      preferredBanks: [],
      preferredCondition: false,
      recommendationList: [],
    };
  },
  methods: {
    recommendProducts() {
    axios
      .post(`${API_URL}/products/recommend-products/`, {
        product_type: this.productType,
        amount: this.amount,
        duration: this.duration,
        preferred_banks: this.preferredBanks,
        preferred_condition: this.preferredCondition,
      })
      .then((res) => {
        this.recommendationList = res.data['추천 상품'];
      })
      .catch((err) => {
        console.error(err);
      });
    },
    calculateExpectedAmount(product) {
      if (this.productType === '예금') {
    // 예금 계산식
        return this.amount + (this.amount * product.이율 * this.duration) / 100;
      } else if (this.productType === '적금') {
    // 적금 계산식
        return this.amount + (this.amount * product.이율 * this.duration * 12) / 100;
    }
      return 0; // 기타 경우에는 0으로 처리하거나 적절한 값으로 수정하세요.
    },
  },
};
</script>
    