<template>
    <div class="flex flex-col justify-center items-center">

        <div class="window">
            <div class="top">
                <img src="../assets/tiny_logo.png" alt="">
                <span>Designer.exe</span>
            </div>

            <div class="content flex flex-col items-center">
                <span class="content-title">Designer</span>
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
                        <div class="flex justify-start">
                            <div class="item-box" @click="onTechChange('UI/UX')">
                                <span class="item center"
                                    :style="{ backgroundColor: selectedTechs.includes('UI/UX') ? '' : '#D5D5D5' }">UI/UX</span>
                                <img v-if="selectedTechs.includes('UI/UX')" src="../assets/icon_clear.png" alt="">
                            </div>
                            <div class="item-box" @click="onTechChange('PM')">
                                <span class="item center"
                                    :style="{ backgroundColor: selectedTechs.includes('PM') ? '' : '#D5D5D5' }">PM</span>
                                <img v-if="selectedTechs.includes('PM')" src="../assets/icon_clear.png" alt="">
                            </div>
                            <div class="item-box" @click="onTechChange('Illustration')">
                                <span class="item center"
                                    :style="{ backgroundColor: selectedTechs.includes('Illustration') ? '' : '#D5D5D5' }">Illustration</span>
                                <img v-if="selectedTechs.includes('Illustration')" src="../assets/icon_clear.png"
                                    alt="">
                            </div>
                            <div class="item-box" @click="onTechChange('Full Stack')">
                                <span class="item center"
                                    :style="{ backgroundColor: selectedTechs.includes('Full Stack') ? '' : '#D5D5D5' }">Full
                                    Stack</span>
                                <img v-if="selectedTechs.includes('Full Stack')" src="../assets/icon_clear.png" alt="">
                            </div>

                        </div>

                        <!-- </div> -->

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
                        <img :src="item.avatar" alt="">
                        <span class="name">{{ item.name }}</span>
                        <div class="line" style="width: 208px;"></div>
                        <span class="des">{{ item.description }}</span>
                        <div class="flex justify-end w-full mr-5 mb-2.5">
                            <div class="tag-item" v-for="t in item.tag" :key="t">{{ t }}</div>
                        </div>

                    </div>
                    <i v-if="filtedBuilders.length > 4"></i>
                    <i v-if="filtedBuilders.length > 4"></i>
                </div>

            </div>
        </div>

        <div class="line" style="width: 1130px; margin-top: 167px;"></div>
        <div class="copy-right">© 2021 <span class="">NONCE GEEK STUDIO.</span> All rights reserved</div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { fetchArtists } from '../utils'

const builders = ref([]);
onMounted(() => {
    fetchArtists().then(response => builders.value = response);
});

let selectedTechs = ref(['UI/UX']);
const isShowSelectContent = ref(true);
const filtedBuilders = computed(() => {
    return builders.value.filter(builder => {
        return builder.tag.some(tag => selectedTechs.value.includes(tag));
    });
});

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
    height: 53px;
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