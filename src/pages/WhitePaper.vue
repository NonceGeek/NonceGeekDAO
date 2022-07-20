<template>
  <div class="flex flex-col items-center md">
    <article className="markdown-body mdh1" v-html="html"/>
  </div>
  <div class="line" style="width: 1130px; margin-top: 50px;"></div>
  <div class="copy-right">© 2021 <span class="">NONCE GEEK STUDIO.</span> All rights reserved</div>
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
    created() {
      // 处理标签居中
      this.html = html.replace(/h1/g,"h1 align=\"center\"")
    }
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

  .copy-right {
    text-align: center;
    font-family: 'Source Han Sans CN';
    font-style: normal;
    font-weight: 400;
    font-size: 10px;
    line-height: 15px;
    color: white;
    padding-top: 20px;
    padding-bottom: 60px;
  }
  
  .copy-right>span {
    font-weight: bold;
  }
</style>