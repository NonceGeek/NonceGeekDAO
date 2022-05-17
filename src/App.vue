<script setup>
import Head from './components/Head.vue'
import Home from './pages/Home.vue'
</script>

<template>
  <div class="main-bg">
    <Head />
    <Home />
  </div>
</template>

<style>
body {
  overflow: hidden;
}
.main-bg {
  background-image: url('./assets/main_bg.png');
  background-size: cover;
  background-repeat: no-repeat;
  width: 100vw;
  height: 100vh;
}
@font-face {
  font-family: 'FFF Urban';
  src: url('./assets/FFF Urban.ttf');
}
</style>
