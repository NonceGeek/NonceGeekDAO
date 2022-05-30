<template>
    <div class="flex flex-col justify-center items-center">

        <div class="window">

            <div class="follow flex flex-col justify-start items-center">
                <span class="follow-bar flex justify-center items-center">Follow Us</span>
                <div class="flex flex-col justify-evenly" style="height: calc(100% - 22px);">
                    <div class="follow-item-box flex justify-center items-center">
                        <a href="https://twitter.com/Web3dAppCamp">
                            <img src="../assets/twitter.png" alt="twitter">
                        </a>
                    </div>
                    <span class="line" style="width: 37px;"></span>
                    <div class="follow-item-box flex justify-center items-center">
                        <a href="https://github.com/WeLightProject">
                            <img src="../assets/github.png" alt="github">
                        </a>
                    </div>
                </div>
            </div>

            <div class="top">
                <img src="../assets/tiny_logo.png" alt="">
                <span>Catalogue.exe</span>
            </div>

            <div class="content flex flex-col items-center">
                <span class="content-title">Web3.0 dApp Camp</span>
                <span class="line" style="width: 491px; margin-bottom: 18px;"></span>

                <div class="camp-item flex justify-between items-center" v-for="item in camps" :key="item.title">
                    <div class="left flex flex-col justify-between">
                        <span class="title">{{ item.title }}</span>
                        <div class="flex justify-between items-end ml-3">
                            <div class="flex items-start">
                                <span class="point mr-2 mt-1.5"></span>
                                <div class="des">{{ item.des }}</div>
                            </div>

                            <div class="flex justify-between items-end" style="width: 200px;">
                                <div class="flex items-end">
                                    <img :src="item.authorImg" alt="">
                                    <span class="author">{{ item.author }}</span>
                                </div>

                                <span class="author">{{ item.time }}</span>
                            </div>
                        </div>
                    </div>
                    <img class="preview-img" :src="item.previewImg" alt="">
                </div>
            </div>
        </div>

        <img class="camp-bottom" src="../assets/series_bottom.png" alt="camp bottom">
    </div>
</template>

<script setup>
import { ref } from 'vue'
import preview_youtube from '../assets/preview_youtube.png'
import preview_wechat from '../assets/preview_wechat.png'
import preview_github from '../assets/preview_github.png'
import leeduckgo from '../assets/leeduckgo.png'

const camps = ref([
    {
        title: '【0x09】Deploy your contract to polygon testnet & verify it on polygonscan ',
        author: 'leeduckgo',
        authorImg: leeduckgo,
        time: '7days ago',
        previewImg: preview_youtube,
        des: 'Metamask 添加 Godwoken 网络，领取测试币 通过 Remix 在 Godwoken 部署合约 ...',
    },
    {
        title: '【0x03 Project】尝试运行scaffold-eth！',
        author: 'leeduckgo',
        authorImg: leeduckgo,
        time: '2021.11.14',
        previewImg: preview_wechat,
        des: '从 Project 0x03 开始，我们开始正式接触 dApp 了第一个任务，把 Scaffold-Eth 脚手架运行起来！',
    },
    {
        title: '【0x02 Project】使用 eth.build 调用智能合约',
        author: 'leeduckgo',
        authorImg: leeduckgo,
        time: '2021.11.09',
        previewImg: preview_github,
        des: '在今天的 Project 0x02 中，我们来实践如何通过eth.build来进行智能合约的调取！',
    },
    {
        title: '【0x01 Project】基于 eth.build 可视化理解区块链基础原理之一',
        author: 'leeduckgo',
        authorImg: leeduckgo,
        time: '2021.11.04',
        previewImg: preview_youtube,
        des: '用eth.build实现和以太坊交互 —— 如何发送 eth？',
    },
])
</script>

<style scoped>
.window {
    width: 1120px;
    height: 707px;
    background-color: #D4D4D4;
    margin: 115px auto 0;
    position: relative;
}

.top>img {
    width: 18.84px;
    height: 37.69px;
    margin-left: 15px;
    margin-right: 26px;
}

.top>span {
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 20px;
    line-height: 24px;
    color: #02083C;
    text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.content {
    width: 1108px;
    height: 627px;
    background-color: #E7E7E7;
    margin: 0 auto;
    border-top: 1px solid black;
    border-left: 1px solid black;
    border-right: 1px solid white;
    border-bottom: 1px solid white;

}

.content-title {
    font-family: 'FFF Urban';
    font-style: normal;
    font-weight: 400;
    font-size: 48px;
    line-height: 66px;
    color: #02083C;
    margin-top: 36px;
    margin-bottom: 11px;
}

.camp-item {
    width: 1039px;
    height: 113px;
    border-top: 1px solid white;
    border-left: 1px solid white;
    border-right: 1px solid black;
    border-bottom: 1px solid black;
    margin-bottom: 10px;
    padding-left: 26px;
    padding-right: 30px;
}

.left {
    width: 736px;
    height: calc(100% - 18px);
}

.title {
    font-family: 'Source Han Sans CN';
    font-style: normal;
    font-weight: 700;
    font-size: 20px;
    line-height: 30px;
}

.des {
    font-family: 'Source Han Sans CN';
    font-style: normal;
    font-weight: 400;
    font-size: 12px;
    line-height: 18px;
    width: 282px;
}

.author {
    font-family: 'Source Han Sans CN';
    font-style: normal;
    font-weight: 400;
    font-size: 12px;
    line-height: 18px;
    color: #484848;
    margin-left: 5px;
}

.preview-img {
    width: 139px;
    height: 88px;
}

.follow {
    position: absolute;
    left: -100px;
    top: 0;
    width: 70px;
    height: 131px;
    background-color: #D4D4D4;
}

.follow-bar {
    width: 70px;
    height: 22px;
    background-color: #71B6C6;
    color: #02083C;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 13px;
    line-height: 16px;
}

.follow-item-box {
    width: 37px;
    height: 37px;
    background-color: #E7E7E7;
}

.camp-bottom {
    width: 1117px;
    height: 46px;
    margin-top: 100px;
}
</style>