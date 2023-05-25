<template>
  <div class="container">
    <div class="center">
      <h1>환율 계산</h1>
      <br>
    </div>
    <div class="row">
      <h4 class="left">국가 / 화폐를 선택해주세요</h4>
      <div class="left">
        <select v-model="selectedCurrency" @change="updateCurrency">
          <option v-for="currency in countryList" :key="currency.code" :value="currency.code">
            {{ currency.name }}
          </option>
        </select>
      </div>
    </div>
    <div class="row">
      <div class="center">
        <input type="number" v-model="koreanWonAmount" @input="calculateExchangeToForeign" placeholder="한국 원 입력" style="width: 800px;">
      </div>
      <div class="right">
        <p v-if="selectedCurrency && conversion_rates">{{ koreanWonAmount }}원은 {{ convertedAmount }} {{ getCurrencyName(selectedCurrency) }}입니다.</p>
      </div>
    </div>
    <div class="row">
      <div class="center">
        <input type="number" v-model="foreignAmount" @input="calculateExchangeToWon" placeholder="금액 입력" style="width: 800px;">
      </div>
      <div class="right">
        <p v-if="selectedCurrency && conversion_rates">{{ foreignAmount }} {{ getCurrencyName(selectedCurrency) }}은/는 {{ convertedWon }}원입니다.</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 70vh;
  margin: auto;
  margin-top: 50px;
  text-align: center;
  border: 2px solid black;
  border-radius: 10px;
}

.row {
  display: flex;
  justify-content: space-between;
  width: 800px;
  align-items: center;
  margin-bottom: 20px;
}

.left {
  text-align: left;
  margin-bottom: 20px;
}

.center {
  text-align: center;
  margin-bottom: 10px;
}

.right {
  text-align: right;
  margin-bottom: 30px;
}
</style>









<script>
  import axios from "axios";
  
  export default {
    name: "Exchange",
    data() {
      return {
        countryList: [
          { code: "USD", name: "미국 달러" },
          { code: "EUR", name: "유로" },
          { code: "JPY", name: "일본 엔화" },
          { code: "GBP", name: "파운드" },
          { code: "AUD", name: "호주 달러"},
          { code: "CAD", name: "캐나다 달러"},
          { code: "CHF", name: "스위스 프랑"},
          { code: "CNY", name: "중국 위안화" },
          { code: "SEK", name: "스웨덴 크로나" },
          { code: "MXN", name: "멕시코 페소"},
          { code: "NZD", name: "뉴질랜드 달러"},
          { code: "SGD", name: "싱가포르 달러"},
          { code: "HKD", name: "홍콩 달러"},
          { code: "NOK", name: "노르웨이 크로네"},
          { code: "TRY", name: "터키 리라"},
          { code: "INR", name: "인도 루피"},
          { code: "RUB", name: "러시아 루블"},
          { code: "THB", name: "태국 바트"},
          { code: "VND", name: "베트남 동"},
        ],
        selectedCurrency: "",
        koreanWonAmount: null,
        foreignAmount: null,
        conversion_rates: null,
        convertedAmount: null,
        convertedWon: null,
      };
    },
    methods: {
      updateCurrency() {
        this.convertedAmount = null;
      },
      calculateExchangeToForeign() {
        if (this.selectedCurrency && this.conversion_rates && this.koreanWonAmount) {
          const rate = this.conversion_rates[this.selectedCurrency];
          this.convertedAmount = (this.koreanWonAmount * rate).toFixed(2);
        } else {
          this.convertedAmount = null;
        }
      },
      calculateExchangeToWon() {
        if (this.selectedCurrency && this.conversion_rates && this.foreignAmount) {
          const rate = this.conversion_rates[this.selectedCurrency];
          this.convertedWon = (this.foreignAmount / rate).toFixed(2);
        } else {
          this.convertedWon = null;
        }
      },
      getData() {
        const url = "https://v6.exchangerate-api.com/v6/79beaa5e2b28af314307a45d/latest/KRW";
  
        axios
          .get(url)
          .then((response) => {
            this.conversion_rates = response.data.conversion_rates;
          })
          .catch((error) => {
            console.log(error);
          });
      },
      getCurrencyName(code) {
        const currency = this.countryList.find((item) => item.code === code);
        return currency ? currency.name : "";
      },
    },
    mounted() {
      this.getData();
    },
  };
</script>
  