<script setup>
import { ref } from "@vue/reactivity";
import router from '../router';

const heads = ref([{
    name: 'home',
    des: 'Introduction',
}, {
    name: 'series',
    des: 'TaiShang Series',
}, {
    name: 'camp',
    des: 'Web3.0 dApp Camp',
}, {
    name: 'builders',
    des: 'Builders',
}, {
    name: 'partners',
    des: 'Partners',
}, {
    name: 'about',
    des: 'About',
}]);

const nav = (name) => {
    router.push({ name: name });
}
</script>

<template>
    <div class="container">
        <img src="../assets/home_icon.png" class="home-icon" alt="home">
        <div class="head-item" v-for="item in heads" :key="item.name" @click="nav(item.name)">{{
                item.des
        }}</div>
    </div>
</template>

<style scoped>
.container {
    width: 1120px;
    height: 52.42px;
    margin: 0 auto;
    padding-top: 34px;
    font-family: 'FFF Urban';
    font-style: normal;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
}

.home-icon {
    width: 142px;
    height: 100%;
}

.head-item {
    height: 35px;
    padding: 3px 10px;
    color: white;
    vertical-align: middle;
    background-color: #02083C;
    font-weight: 400;
    font-size: 20px;
    line-height: 35px;
    border-right: 4px solid #B7E3ED;
    border-bottom: 4px solid #B7E3ED;
}

.head-item:hover {
    color: #02083C;
    background-color: white;
    border-right: none;
    border-bottom: none;
    border-top: 4px solid #B7E3ED;
    border-left: 4px solid #B7E3ED;
}
</style>