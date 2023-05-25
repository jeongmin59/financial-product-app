<template>
<div>
    <p>{{ product.kor_co_nm }}</p>
    <router-link :to="{
    name: 'SavingDetailView',
    params: { fin_prdt_cd: product.fin_prdt_cd }}"><p>{{ product.fin_prdt_nm }}</p>
    </router-link>
    <SavingDetailView />
</div>
</template>
  
<script>
import SavingDetailView from '@/components/products/SavingDetail.vue'

export default {
  name: 'SavingListItemView',
  props: {
    product: Object,
  },
  components: {
    SavingDetailView
  }
}
</script>