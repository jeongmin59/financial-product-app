<template>
<div class="products">
  <h1>금융 상품</h1>
  <DespositListView />
  </div>
</template>

<script>
import DespositListView from '@/views/products/DespositList.vue'

export default {
  name: 'ProductsView',
  components: {
    DespositListView,
  }

}
</script>

<style>

</style>