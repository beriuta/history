<template>
  <div>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" >
      <el-menu-item index="/">甜点</el-menu-item>
      <el-menu-item index="/coffee">咖啡</el-menu-item>
      <el-menu-item index="/cake">蛋糕</el-menu-item>
      <el-menu-item index="/toast">吐司</el-menu-item>
      <el-menu-item index="/pudding">水果补丁</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
  export default {
    name: "MyHead",
    data(){
      return {
        activeIndex:'/'
      }
    }
  }
</script>

<style scoped>

</style>
