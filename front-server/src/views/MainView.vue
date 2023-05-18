<template>
  <div class="main">
    <!-- 메인 영역 -->
    <!-- <img src="@/assets/logo.png" alt="GJMG logo"> -->

    <nav>
      <router-link :to="'/community'">커뮤니티</router-link>
    </nav>

    <router-view></router-view>

  </div>
</template>

<script>
// import CommunityView from '@/views/Community/CommunityView.vue'

export default {
  // components: {
  //   CommunityView,
  // }
}
</script>

<style>
</style>
