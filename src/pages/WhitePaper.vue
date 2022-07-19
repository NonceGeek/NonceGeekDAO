<template>
  <div class="flex flex-col justify-between items-center h-screen md">
    <article className="markdown-body mdh1" v-html="html"/>
  </div>
</template>

<script>
  import 'github-markdown-css/github-markdown.css';
  import {html} from '../assets/NonceGeekDAO Whitepaper v1.md';
  
  export default {
    data() {
      return {
        html
      };
    },
  };
</script>
<style scoped>
  .md{
    height: auto;
    margin: 80px auto ;
    padding: 50px;
    width: 80%;
    background-color: #FFFFFF;
  }
  article h1{
    text-align: center;
  }
</style>