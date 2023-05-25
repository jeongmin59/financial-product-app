<template>
<div>
  <p>{{ product.kor_co_nm }}</p>
  <router-link :to="{
    name: 'DepositDetailView',
    params: { fin_prdt_cd: product.fin_prdt_cd }}"><p>{{ product.fin_prdt_nm }}</p>
  </router-link>
</div>
</template>

<script>

export default {
  name: 'DepositListItemView',
  props: {
    product: Object,
  },
}
</script>
