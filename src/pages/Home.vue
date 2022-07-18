<script setup>
// TODO：背景动起来 + 蒸汽波音乐
</script>

<template>
    <div class="box center">
        <div class="window">
            <img class="home-bg" src="../assets/home_bg.png" alt="">

            <span class="title">Nonce Geek DAO.exe</span>
            <span class="absolute top-[265px] left-[140px] font-blox text-bluedeep text-7xl">NoNceGEEK</span>
            <span class="absolute top-[360px] left-[273px] font-minecraft text-bluedeep text-3xl">DAO</span>

            <img class="sub-bg" src="../assets/sub_bg.png" alt="sub bg">
        </div>

    </div>
</template>

<style scoped>
.box {
    width: calc(100vw - 86px);
    height: 100vh;
}

.window {
    position: relative;
    width: 1202px;
    height: 563px;
}

.home-bg {
    width: 1202px;
    height: 563px;
    position: absolute;
    top: 105px;
    left: 80px;
}

.title {
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 12px;
    line-height: 15px;
    color: #3c0a02;
    position: absolute;
    top: 204px;
    left: 100px;
}

.sub-bg {
    width: 454px;
    height: 181px;
    position: absolute;
    top: 487px;
    left: 81px;
}
</style>