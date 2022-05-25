<script setup>

</script>

<template>
    <div class="box center">
        <div class="window">
            <img class="home-bg" src="../assets/home_bg.png" alt="">
            <span class="title">Nonce Geek studio.exe</span>
            <img class="home-icon-big" src="../assets/home_icon_big.png" alt="home icon">
            <img class="geek-studio" src="../assets/geek_studio.png" alt="geek studio">
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

.home-icon-big {
    width: 304px;
    height: 112px;
    position: absolute;
    top: 249px;
    left: 148px;
}

.geek-studio {
    width: 289px;
    height: 36px;
    position: absolute;
    top: 366px;
    left: 155px;
}

.sub-bg {
    width: 454px;
    height: 181px;
    position: absolute;
    top: 487px;
    left: 81px;
}
</style>