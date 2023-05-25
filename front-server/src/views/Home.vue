<template>
<div class="home">
  <header class="header">
    <h1>금융 상품 비교</h1>
    <div>당신이 원하는 예금, 적금을 비교해보세요! </div>
    <a href="/profile">ProfileView</a>
  </header>

  <div class="row row-cols-1 row-cols-md-3 g-3">
    <div class="col">
      <div class="card h-100">
        <a href="/products" class="custom-link">
          <div class="card-body">
            <h5 class="card-title">금융 상품</h5>
            <p class="card-text">지금 바로 예금, 적금을 비교해보세요!</p>
          </div>
        </a>
      </div>
    </div>
    <div class="col">
      <div class="card h-100">
        <a href="#" class="custom-link">
          <div class="card-body">
            <h5 class="card-title">은행 찾기</h5>
            <p class="card-text">원하는 위치에 있는 모든 은행을 찾아볼 수 있습니다.</p>
          </div>
        </a>
      </div>
    </div>
    <div class="col">
      <div class="card h-100">
        <a href="/Exchange" class="custom-link">
          <div class="card-body">
            <h5 class="card-title">환율 계산</h5>
            <p class="card-text">지금 환율이 얼마 정도지? 직접 계산해보세요!</p>
          </div>
        </a>
      </div>
    </div>
  </div>

  <div class="row row-cols-1 row-cols-md-2 g-3">
    <div class="col">
      <div class="card h-100">
        <a href="/community" class="custom-link">
          <div class="card-body">
            <h5 class="card-title">게시판</h5>
            <p class="card-text">최근 글 불러오기 ㄱ-</p>
          </div>
        </a>
      </div>
    </div>
    <div class="col">
      <div class="card h-100">
        <a href="/recommend-products" class="custom-link">
          <div class="card-body">
            <h5 class="card-title">금융 상품 추천 바로 가기</h5>
            <p class="card-text">개인 맞춤 추천 시스템</p>
          </div>
        </a>
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
.custom-link {
  text-decoration: none; /* 밑줄 제거 */
  color: #000000; /* 원하는 색상으로 변경 */
}

</style>

