<template>
    <div class="flex flex-col justify-between items-center h-screen">
        <i></i>
        <div class="window">
            <div class="top" style="width: 716px;">
                <img src="../assets/tiny_logo.png" alt="">
                <span>Contact Us.exe</span>
            </div>
            <div class="content flex justify-between">
                <img class="qrcode" src="../assets/qrcode.png" alt="">
                <div class="contact-us-box flex flex-col justify-between items-center">
                    <i></i>
                    <span class="contact-us">Contact Us</span>
                    <div class="flex items-end">
                        <img src="../assets/wechat.png" alt="">
                        <span class="wechat-id">lee_duck_go</span>
                    </div>
                    <div class="flex items-end">
                        <span class="wechat-id">Telegram: @leeduckgo </span>
                    </div>
                </div>
                <div style="width: 26.5px; height: 356px;" class="flex flex-col justify-between">
                    <span class="scroll-top center">
                        <span class="up-triangle"></span>
                    </span>
                    <span class="scroll-middle"></span>
                    <span class="scroll-bottom center">
                        <span class="down-triangle"></span>
                    </span>
                </div>
            </div>
        </div>
        <img class="about-bottom" src="../assets/series_bottom.png" alt="about bottom">
    </div>
</template>

<style scoped>
.window {
    width: 728px;
    height: 424px;
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
    width: 714px;
    margin-left: 9.95px;
    margin-right: 6.5px;
    border-top: 1px solid black;
    border-left: 1px solid black;
    background: #E5E5E5;
}

.qrcode {
    width: 355.48px;
    height: 355.48px;
}

.contact-us-box {
    /* width: auto; */
}

.contact-us {
    font-family: 'FFF Urban';
    font-style: normal;
    font-weight: 400;
    font-size: 40px;
    line-height: 20px;
}

.wechat-id {
    font-family: 'FFF Urban';
    font-style: normal;
    font-weight: 400;
    font-size: 24px;
    line-height: 33px;
    margin-left: 10px;
}

.scroll-top {
    width: 26.5px;
    height: 26.5px;
    background: #D5D5D5;
    box-shadow: inset 1px 1px 0px #FFFFFF, inset -1px -1px 0px rgba(0, 0, 0, 0.8), inset 1px 1px 1px #E5E5E5;
}

.up-triangle {
    width: 0;
    border-left: 7px solid transparent;
    border-right: 7px solid transparent;
    border-bottom: 15px solid black;
}

.scroll-middle {
    width: 26px;
    height: 294px;
    background: #D5D5D5;
    box-shadow: inset 1px 1px 0px #FFFFFF, inset -1px -1px 0px rgba(0, 0, 0, 0.8), inset 1px 1px 1px #E5E5E5;
}

.scroll-bottom {
    width: 26.5px;
    height: 26.5px;
    background: #D5D5D5;
    box-shadow: inset 1px 1px 0px #FFFFFF, inset -1px -1px 0px rgba(0, 0, 0, 0.8), inset 1px 1px 1px #E5E5E5;
}

.down-triangle {
    width: 0;
    border-left: 7px solid transparent;
    border-right: 7px solid transparent;
    border-top: 15px solid black;
}

.about-bottom {
    width: 1117px;
    height: 46px;
    margin-top: 84px;
}
</style>