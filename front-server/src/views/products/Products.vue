<template>
  <div class="products">
    <h1>금융 상품</h1>
    <DepositListView />
    <SavingListView />
    </div>
  </template>
  
  <script>
  import DepositListView from '@/views/products/DepositList.vue'
  import SavingListView from '@/components/products/SavingList.vue'
  
  export default {
    name: 'ProductsView',
    components: {
      DepositListView,
      SavingListView,
    }
  
  }
  </script>
  
  <style>
  
  </style>