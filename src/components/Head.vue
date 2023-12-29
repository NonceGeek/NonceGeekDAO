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
    name: 'projects',
    des: 'cOOl Projects',
}, 
{
    name: 'github',
    des: 'Github',
},
{
    name: 'buidlers',
    des: 'Buidlers',
}, {
//     name: 'partners',
//     des: 'Partners',
// }, {
    name: 'about',
    des: 'About',
}]);

const clickedItem = ref('home');

const nav = (name) => {
    clickedItem.value = name;
    if(name=="partners"){
        window.location.href = "https://noncegeek.notion.site/822c09f42d324d00b3e152e74997322b?v=105eea10cf4b4ec1928984221fdc0408";
    }else if(name=="buidlers"){
        window.location.href = "https://noncegeek.notion.site/7e57db9727444b41ba963ce2e5e9ca5a?v=3571cec630584c0b9e9a4f2349a8970c";
    }else if(name=="projects"){
        window.location.href = "https://projects.noncegeek.com";
    }else if(name=="github"){
        window.location.href = "https://github.com/NonceGeek";
    }else{
        router.push({ name: name });
    }
}

</script>

<template>
    <div class="box">
        <span class="font-blox text-blue text-5xl">&nbsp;&nbsp;NoNceGEEK DAO</span>
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