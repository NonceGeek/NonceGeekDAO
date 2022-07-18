<script setup>
import { ref } from "@vue/reactivity";
import router from '../router';

const heads = ref([{
    name: 'home',
    des: 'Index',
}, {
    name: 'whitepaper',
    des: 'WhitePaper v1',
},{
    name: 'series',
    des: 'TaiShang Series',
}, {
    name: 'builders',
    des: 'Builders',
},
{
    name: 'artist',
    des: 'Artist',
},
{
    name: 'partners',
    des: 'Partners',
}, {
    name: 'about',
    des: 'About',
}]);

const clickedItem = ref('home');

const nav = (name) => {
    clickedItem.value = name;
    router.push({ name: name });
}

</script>

<template>
    <div class="box">
        <span class="font-blox text-blue text-5xl">NoNceGEEK</span>
        <div class="navs flex justify-end items-center">
            <div
                :class="{ 'ml-3 head-item': true, 'head-item-clicked': clickedItem === item.name }"
                v-for="item in heads"
                :key="item.name"
                @click="nav(item.name)"
            >
                {{item.des}}
            </div>
        </div>
    </div>
</template>

<style scoped>
.box {
    width: 1320px;
    height: 86.42px;
    margin: 0 auto;
    padding-top: 34px;
    font-family: 'FFF Urban';
    font-style: normal;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
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

.head-item-clicked {
    color: #02083C;
    background-color: white;
    border-right: none;
    border-bottom: none;
    border-top: 4px solid #B7E3ED;
    border-left: 4px solid #B7E3ED;
}
</style>