<script setup>
import Head from './components/Head.vue'
import Home from './pages/Home.vue'
</script>

<template>
  <div class="main-bg">

    <Head />
    <router-view></router-view>
  </div>
</template>

<style>
.main-bg {
  background-image: url('./assets/main_bg.png');

}

@font-face {
  font-family: 'FFF Urban';
  src: url('./assets/FFF Urban.ttf');
}

@font-face {
  font-family: 'Inter';
  src: url('./assets/Inter.ttf');
}
</style>
