<template>
    <div class="flex flex-col justify-center items-center">

        <div class="window">
            <div class="top">
                <img src="../assets/tiny_logo.png" alt="">
                <span>Buidlers.exe</span>
            </div>

            <div class="content flex flex-col items-center">
                <span class="content-title">Buidlers</span>
                <span class="line" style="width: 193px; margin-bottom: 18px;"></span>
                <span class="select-title">Nonce Geek People</span>

                <div class="select flex flex-col justify-start">
                    <div class="flex">
                        <div class="select-box flex justify-start items-center">

                            <div class="item-box" v-for="item in selectedTechs" :key="item">
                                <span class="item center">{{ item }}</span>
                                <img src="../assets/icon_clear.png" alt="">
                            </div>

                        </div>
                        <div class="click-rect" @click="onSelectContentChange">
                            <div class="down-triangle"></div>
                        </div>
                    </div>
                    <div class="select-content flex flex-col justify-evenly" v-if="isShowSelectContent">
                        <div class="flex justify-evenly">
                            <div class="flex" style="width: 354px;">
                                <span class="item-title">合约技术栈</span>
                                <div class="item-box" @click="onTechChange('Solidity')">
                                    <span class="item center"
                                        :style="{ backgroundColor: selectedTechs.includes('Solidity') ? '' : '#D5D5D5' }">Solidity</span>
                                    <img v-if="selectedTechs.includes('Solidity')" src="../assets/icon_clear.png"
                                        alt="">
                                </div>
                                <div class="item-box" @click="onTechChange('Move')">
                                    <span class="item center"
                                        :style="{ backgroundColor: selectedTechs.includes('Move') ? '' : '#D5D5D5' }">Move</span>
                                    <img v-if="selectedTechs.includes('Move')" src="../assets/icon_clear.png" alt="">
                                </div>
                            </div>

                            <div class="flex " style="width: 354px;">
                                <span class="item-title">前端技术栈</span>
                                <div class="item-box" @click="onTechChange('React')">
                                    <span class="item center"
                                        :style="{ backgroundColor: selectedTechs.includes('React') ? '' : '#D5D5D5' }">React</span>
                                    <img v-if="selectedTechs.includes('React')" src="../assets/icon_clear.png" alt="">
                                </div>
                                <div class="item-box" @click="onTechChange('scaffold-eth')">
                                    <span class="item center"
                                        :style="{ backgroundColor: selectedTechs.includes('scaffold-eth') ? '' : '#D5D5D5' }">scaffold-eth</span>
                                    <img v-if="selectedTechs.includes('scaffold-eth')" src="../assets/icon_clear.png"
                                        alt="">
                                </div>
                            </div>
                        </div>

                        <div class="flex justify-evenly">
                            <div class="flex" style="width: 354px;">
                                <span class="item-title">后端技术栈</span>
                                <div class="item-box" @click="onTechChange('Elixir')">
                                    <span class="item center"
                                        :style="{ backgroundColor: selectedTechs.includes('Elixir') ? '' : '#D5D5D5' }">Elixir</span>
                                    <img v-if="selectedTechs.includes('Elixir')" src="../assets/icon_clear.png" alt="">
                                </div>
                                <div class="item-box" @click="onTechChange('Rust')">
                                    <span class="item center"
                                        :style="{ backgroundColor: selectedTechs.includes('Rust') ? '' : '#D5D5D5' }">Rust</span>
                                    <img v-if="selectedTechs.includes('Rust')" src="../assets/icon_clear.png" alt="">
                                </div>
                            </div>

                            <div class="flex" style="width: 354px;">
                                <span class="item-title">区块链技术栈</span>
                                <div class="item-box" @click="onTechChange('ethereum')">
                                    <span class="item center"
                                        :style="{ backgroundColor: selectedTechs.includes('ethereum') ? '' : '#D5D5D5' }">ethereum</span>
                                    <img v-if="selectedTechs.includes('ethereum')" src="../assets/icon_clear.png"
                                        alt="">
                                </div>
                                <div class="item-box" @click="onTechChange('arweave')">
                                    <span class="item center"
                                        :style="{ backgroundColor: selectedTechs.includes('arweave') ? '' : '#D5D5D5' }">arweave</span>
                                    <img v-if="selectedTechs.includes('arweave')" src="../assets/icon_clear.png" alt="">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="line" style="width: 1030px; margin-top: 31px; margin-bottom: 46px;"></div>

                <div class="card-box flex justify-between flex-wrap">
                    <div class="card flex flex-col justify-between items-center" v-for="item in filtedBuilders"
                        :key="item.name">
                        <div class="card-top flex justify-end items-center">
                            <div></div>
                            <div></div>
                            <div></div>
                        </div>
                        <img :src="item.img" alt="">
                        <span class="name">{{ item.name }}</span>
                        <span class="des">{{ item.des }}</span>
                        <div class="github flex">
                            <img src="../assets/github.png" alt="">
                            <span>{{ item.github }}</span>
                        </div>
                        <div class="line" style="width: 208px;"></div>
                        <div class="achi-item flex items-start" v-for="achi in item.achievements" :key="achi">
                            <div class="point" style="margin-top: 8px; margin-right: 5px;"></div>
                            <div>{{ achi }}</div>
                        </div>
                        <div class="flex justify-end w-full mr-5 mb-2.5">
                            <div class="tag-item" v-for="t in item.tag" :key="t">{{ t }}</div>
                        </div>

                    </div>
                    <i v-if="filtedBuilders.length > 8"></i><i v-if="filtedBuilders.length > 8"></i><i
                        v-if="filtedBuilders.length > 8"></i>
                </div>

            </div>
        </div>

        <div class="line" style="width: 1130px; margin-top: 167px;"></div>
        <div class="copy-right">© 2021 <span class="">NONCE GEEK STUDIO.</span> All rights reserved</div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const builders = ref([
    {
        name: '李大狗',
        img: '/src/assets/avatar_lidagou.png',
        des: '面向酷炫编程',
        github: 'https://github.com/leeduckgo',
        achievements: ['1小时理解比特币系统', '区块链与共识机制演变史'],
        tag: ['Solidity'],
    },
    {
        name: '王宁波',
        img: '/src/assets/avatar_wangningbo.png',
        des: '学习区块链开发途中的平头哥',
        github: 'https://github.com/hqwangningbo',
        achievements: ['构建你的第一条Substrate chain并与之交互', 'Substrate-node-template模板中的pallet-template源码分析'],
        tag: ['scaffold-eth'],
    },
    {
        name: '汤会枫',
        img: '/src/assets/avatar_tanghuifeng.png',
        des: '懂点区块链和云计算的后端开发',
        github: 'https://github.com/99Kies',
        achievements: ['分布式数字身份-从创建一个Weidentity开始', '理解和验证Pbft共识机制'],
        tag: ['Solidity', 'scaffold-eth'],
    },
    {
        name: '何伟',
        img: '/src/assets/avatar_hewei.png',
        des: '生命不息  学习不止',
        github: 'https://github.com/Dream4ever',
        achievements: ['手写一个音频播放器', '解决 MySQL CPU 占用高的问题'],
        tag: ['scaffold-eth'],
    },
    {
        name: '姚溯宁',
        img: '/src/assets/avatar_yaoshuoning.png',
        des: '一直是个非传统的人，数学专业的前端开发',
        github: 'https://github.com/fewwwww',
        achievements: ['浅谈Dfinity的云计算+区块链', 'React组件拖拽改变大小功能'],
        tag: ['Solidity'],
    },
    {
        name: '肖越',
        img: '/src/assets/avatar_xiaoyue.png',
        des: '一个懂点网络安全和区块链的信安大三学僧',
        github: 'https://github.com/xiaoyue2019',
        achievements: ['合约安全之越权攻击', 'FISCO BCOS多机部署之单群组双机构双节点组网模式'],
        tag: ['Solidity'],
    },
    {
        name: 'Henry Liu',
        img: '/src/assets/avatar_henryliu.png',
        des: '到现在都没搞懂啥是区块链的菜鸟',
        github: 'https://github.com/Zoombieliu',
        achievements: [],
        tag: ['Solidity'],
    },
    {
        name: '叶开',
        img: '/src/assets/avatar_yekai.png',
        des: '非著名区块链技术讲师',
        github: 'https://github.com/yekai1003',
        achievements: ['看过《斯巴达克斯》吗？里面的反派竟是密码学鼻祖', '比特币和区块链的基石：哈希函数'],
        tag: ['Solidity'],
    },
    {
        name: '蓉儿',
        img: '/src/assets/avatar_ronger.png',
        des: '生成艺术家',
        github: 'https://github.com/lovelyrosa',
        achievements: ['浅谈Dfinity的云计算+区块链', 'React组件拖拽改变大小功能'],
        tag: ['Solidity'],
    },
    {
        name: '黄杰',
        img: '/src/assets/avatar_huangjie.png',
        des: '区块链编程爱好者',
        github: 'https://github.com/Blockchain-Key',
        achievements: ['智能合约实例开发（1）——众筹', '智能合约实例开发（2）——食品溯源', '智能合约开发实例（3）——结婚证书'],
        tag: ['Solidity'],
    }
])

let selectedTechs = ref(['Solidity']);
const isShowSelectContent = ref(true);
const filtedBuilders = computed(() => {
    return builders.value.filter(builder => {
        return builder.tag.some(tag => selectedTechs.value.includes(tag));
    });
});

const filterByTechBuidlers = () => {

}

const onTechChange = (tech) => {
    console.log(tech);
    console.log(selectedTechs.value);
    if (selectedTechs.value.includes(tech)) {
        selectedTechs.value = selectedTechs.value.filter(t => t !== tech);
    } else {
        selectedTechs.value.push(tech);
    }
    console.log(selectedTechs.value);
}

const onSelectContentChange = () => {
    isShowSelectContent.value = !isShowSelectContent.value;
}

</script>

<style scoped>
.window {
    width: 1120px;
    /* height: 1748px; */
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

.select-box {
    width: 981px;
    height: 33px;
    box-shadow: inset 1px 1px 0px rgba(0, 0, 0, 0.8), inset -1px -1px 0px rgba(0, 0, 0, 0.1);
    background: #FFFFFF;
}

.click-rect {
    width: 28px;
    height: 28px;
    background-color: #D5D5D5;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-left: 14px;
    border-top: 1px solid white;
    border-left: 1px solid white;
    border-right: 1px solid black;
    border-bottom: 1px solid black;
}

.down-triangle {
    width: 0;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 10px solid black;
}

.select-content {
    width: 1030px;
    height: 92px;
    box-shadow: inset -1px -1px 1px rgba(0, 0, 0, 0.8), inset 1px 1px 1px rgba(255, 255, 255, 0.8);
    margin-top: 14px;
}

.item-title {
    width: 120px;
}

.item-box {
    position: relative;
    width: 120px;
    height: 21px;
}

.item-box>img {
    position: absolute;
    right: 0;
    top: -2px;
}

.item {
    background-color: #B7E3ED;
    margin-left: 18px;
}

.grey-bg {
    background-color: #D5D5D5;
}

.card-box {
    width: 1032px;
    height: auto;
}

.card {
    width: 249px;
    height: 403px;
    background-color: #D4D4D4;
    margin-bottom: 27px;
}

.card-top {
    width: calc(100% - 6px);
    height: 30px;
    background-color: #71B6C6;
    margin: 3px auto 0px;
}

.card>img {
    width: 208px;
    height: 211px;
    box-shadow: inset 1px 1px 0px #FFFFFF, inset -2px -2px 1px rgba(0, 0, 0, 0.8), inset 2px 2px 1px rgba(255, 255, 255, 0.8);
}

.card-top>div {
    width: 20px;
    height: 20px;
    background-color: white;
    box-shadow: 2px 2px black;
    margin-right: 5px;
}

.name {
    font-family: 'Source Han Sans CN';
    font-style: normal;
    font-weight: 700;
    font-size: 16px;
    line-height: 24px;
}

.des {
    font-family: 'Source Han Sans CN';
    font-style: normal;
    font-weight: 400;
    font-size: 9px;
    line-height: 14px;
}

.github>img {
    width: 12px;
    height: 12px;
    margin-right: 4px;
}

.github>span {
    font-family: 'FFF Urban';
    font-style: normal;
    font-weight: 400;
    font-size: 9px;
    line-height: 12px;
}

.achi-item {
    width: 208px;
    font-family: 'Source Han Sans CN';
    font-style: normal;
    font-weight: 400;
    font-size: 10px;
    line-height: 20px;
}

.tag-item {
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 8px;
    line-height: 10px;
    padding: 2px 5px 2px 5px;
    background-color: #B7E3ED;
}

i {
    width: 249px;
    height: 403px;
    margin-bottom: 27px;
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