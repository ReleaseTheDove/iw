<template>
  <div id="app">
    <!-- <router-link to="/home" tag="button" replace>Home</router-link> -->
    <router-link to="/about">About</router-link>
    <!-- <router-link :to="'/market/'+code">Market</router-link> -->
    <router-link :to="'/kline/'+code">KLine</router-link>
    <keep-alive exclude="Market,About,Kline">
      <router-view/>
    </keep-alive>
  </div>
</template>

<script>

export default {
  name: 'App',
  data () {
    return {
      code: '002425.SZ'
    }
  }
}
</script>

<style>
  /* #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  } */
  @import "./assets/css/base.css";
</style>
