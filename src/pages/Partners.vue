<template>
    <div class="flex flex-col items-center">

        <div class="window">
            <div class="top">
                <img src="../assets/tiny_logo.png" alt="">
                <span>Partners.exe</span>
            </div>

            <div class="content flex flex-col items-center">
                <span class="content-title">Partners</span>
                <span class="line" style="width: 217px; margin-bottom: 18px;"></span>
                <span class="select-title">Nonce Geek Partners</span>

                <div class="card" v-for="item in partners" :key="item.name">
                    <div class="card-top flex justify-end items-center">
                        <div></div>
                        <div></div>
                        <div></div>
                    </div>
                    <div class="card-content flex justify-between items-center">
                        <img class="" :src="item.img" alt="">
                        <div class="v-line" style="height: 180px;"></div>
                        <div class="card-bottom-right flex flex-col justify-evenly">
                            <div>
                                <span class="title">{{ item.title }}</span>
                                <span class="sub-title">{{ item.subTitle }}</span>
                            </div>
                            <div class="line" style="width: 680px;"></div>
                            <span class="des">{{ item.des }}</span>
                        </div>
                    </div>
                </div>
            </div>

        </div>
        <div class="line" style="width: 1130px; margin-top: 50px;"></div>
        <div class="copy-right">© 2021 <span class="">NONCE GEEK STUDIO.</span> All rights reserved</div>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const partners = ref([
    {
        img: '/src/assets/partner_moonbeam.png',
        title: 'Moonbeam',
        subTitle: 'Grant for TaiShang NFT Parser& Wallet',
        des: 'Moonbeam是一条面向开发者的区块链，它致力于提供与现有以太坊开发人员工具链和网络的兼容性。它通过提供完整的EVM、与Web3兼容的API以及将Moonbeam连接到现有以太坊网络的网桥来实现这一点。',
    },
    {
        img: '/src/assets/partner_polygon.png',
        title: 'Polygon',
        subTitle: 'Grant for TaiShang World Generator',
        des: 'Polygon是一个建立在以太坊上的Layer2扩展解决方案上的公链。和以太坊比起来，Polygon的速度、可扩展性和可用性都更加有优势。作为后起之秀，Polygon着重布局在区块链游戏和NFT领域。',
    },
    {
        img: '/src/assets/partner_wanxiang.png',
        title: '万向',
        subTitle: ' Grant for 基于联盟链的合规元宇宙',
        des: '万向区块链是区块链技术研发机构，逐步打造了集万向区块链实验室、万向区块链商业创新咨询、新链加速器、万云等业务于一体的区块链生态平台。',
    },
    {
        img: '/src/assets/partner_starcoin.png',
        title: 'Starcoin',
        subTitle: 'Tokens for 基于 Move-Lang 与 Starcoin 的学术研究',
        des: 'Starcoin 是一个去中心化分层智能合约网络，它旨在提供一种安全的数字资产及去中心化金融运行平台，让区块链能够更低门槛应用在更多领域。',
    },
])
</script>

<style scoped>
.window {
    width: 1120px;
    height: 1414px;
    background-color: #D4D4D4;
    margin-top: 77px;
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
    width: 100%;
    height: calc(100% - 49px);
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

.select-title {
    font-family: 'Source Han Sans CN';
    font-style: normal;
    font-weight: 900;
    font-size: 20px;
    line-height: 30px;
    width: 1030px;
    margin-bottom: 11px;
}

.card {
    width: 1019px;
    height: 263px;
    background-color: #D5D5D5;
    margin-bottom: 18px;
}

.card-top {
    width: calc(100% - 6px);
    height: 30px;
    background-color: #71B6C6;
    margin: 3px auto 0px;
}

.card-top>div {
    width: 20px;
    height: 20px;
    background-color: white;
    box-shadow: 2px 2px black;
    margin-right: 5px;
}

.card-content {
    width: 100%;
    height: calc(100% - 30px);
}

.card-content>img {
    margin-left: 26px;
}

.card-bottom-right {
    width: 756px;
    height: 180px;
    background: #E7E7E7;
    box-shadow: inset 1px 1px 0px rgba(0, 0, 0, 0.8), inset -1px -1px 0px #FFFFFF;
    padding-left: 24px;
    padding-right: 43px;
}

.title {
    font-family: 'Source Han Sans CN';
    font-style: normal;
    font-weight: 900;
    font-size: 40px;
    line-height: 60px;
    color: #303030;
    margin-right: 20px;
}

.sub-title {
    font-family: 'Source Han Sans CN';
    font-style: normal;
    font-weight: 400;
    font-size: 16px;
    line-height: 24px;
    color: #303030;
}

.des {
    font-family: 'Source Han Sans CN';
    font-style: normal;
    font-weight: 400;
    font-size: 16px;
    line-height: 24px;
    color: #737373;
    margin: auto 0;
}

.copy-right {
    font-family: 'Source Han Sans CN';
    font-style: normal;
    font-weight: 400;
    font-size: 10px;
    line-height: 15px;
    color: white;
    margin-top: 20px;
    margin-bottom: 60px;
}

.copy-right>span {
    font-weight: bold;
}
</style>