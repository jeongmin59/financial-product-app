<template>
<div class="home">
<div class="container">
  <div class="header d-flex justify-content-center text-center mt-4">
    <h1>금융 상품 비교
      <h5 class="text mt-3">당신이 원하는 예금, 적금을 찾아보세요! </h5>
    </h1>
  </div>

  <div class="row row-cols-1 row-cols-md-3 g-3 mt-3">
    <div class="col">
      <div class="card mx-1 finance-card">
        <a href="/products" class="custom-link">
          <div class="card-body">
            <h2 class="card-title">금융 상품</h2>
            <p class="card-text">현재 가입할 수 있는 <br> 예금과 적금을 <br> 모두 조회할 수 있습니다.</p>
          </div>
          <!-- <div class="container">
            <div class="row">
              <div class="col d-flex flex-column justify-content-end">
                <a href="/products/deposit-products/" class="btn btn-primary btn-lg card-text">
                  예금
                </a>
              </div>
              <div class="col d-flex flex-column justify-content-end">
                <a href="/products/saving-products/" class="btn btn-primary btn-lg card-text">
                  적금
                </a>
              </div>
            </div>
          </div> -->
        </a>
      </div>
    </div>
    <div class="col">
      <div class="card mx-1 findmap-card">
        <a href="/KakaoMap" class="custom-link">
          <div class="card-body">
            <h2 class="card-title">은행 찾기</h2>
            <p class="card-text">원하는 위치에 있는 <br> 모든 은행 <br> 지금 찾아볼 수 있습니다.</p>
          </div>
        </a>
      </div>
    </div>
    <div class="col">
      <div class="card mx-1 exchange-card">
        <a href="/Exchange" class="custom-link">
          <div class="card-body">
            <h2 class="card-title">환율 계산</h2>
            <p class="card-text">지금 환율이 얼마 정도지? <br><br> 환율 계산기로 <br> 직접 계산해보세요!</p>
          </div>
        </a>
      </div>
    </div>
  </div>

  <div class="row row-cols-1 row-cols-md-1 g-3 mt-4">
    <!-- <div class="col">
      <div class="card mx-1">
        <a href="/community" class="custom-link">
          <div class="card-body">
            <h4 class="card-title">게시판</h4>
            <p class="card-text">최근 글 불러오기 ㄱ-</p>
          </div>
        </a>
      </div>
    </div> -->
    <div class="col">
      <div class="card mx-1 custom-card justify-content-center">
        <a href="/recommend-products" class="custom-link">
          <div class="card-body">
            <h3 class="card-title">금융 상품 추천 바로 가기</h3>
            <p class="card-text text-center">개인 맞춤 추천 시스템을 통해 상품 종류와 금액, 기간 <br> 선호하는 은행에 따라 상품을 추천 받을 수 있습니다. </p>
          </div>
        </a>
      </div>
    </div>
  </div>

</div>  
</div>
</template>

<script>
export default {
  name: 'HomeView',
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');
.home {
  font-family: 'Nanum Gothic', sans-serif;
  /* background-color: #D2E1FF; */
}
.custom-link {
  text-decoration: none; /* 밑줄 제거 */
  color: #000000; /* 원하는 색상으로 변경 */
}
.card {
 height: 300px;
}
.custom-card .card-text {
  margin: 10px auto;
}
.custom-card {
 height: 150px;
 background-color: #046fd9;
 border-radius: 0 16px 0 16px;
 border: none;
}
.finance-card {
  background-color: #699f00;
  border-radius: 0 16px 0 16px;
  border: none;
}
.findmap-card {
  background-color: #02963d;
  border-radius: 0 16px 0 16px;
  border: none;
}
.exchange-card {
  background-color: #008ad2;
  border-radius: 0 16px 0 16px;
  border: none;
}
.card-title {
  font-weight: bold;
  text-align: left;
}
.custom-card .card-title {
  font-weight: bold;
  text-align: center;
}
.card-text {
 margin: 30px auto;
 /* letter-spacing: 1px; */
}
.card-body {
 margin: 10px 10px;
 color: white;
}
/* .mx-1 {
  background-color: blue;
} */

/* :root{
  background-color: aqua;
} */
</style>
