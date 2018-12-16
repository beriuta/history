<template>
  <div id="app">
    <my_header></my_header>
    <router-view></router-view>  <!--这是myheader的router-view-->
  </div>
</template>

<script>
  import MyHeader from "./components/MyHead"

export default {
  name: 'App',
  components: {
      my_header:MyHeader
  }
}
</script>

<style>
</style>
