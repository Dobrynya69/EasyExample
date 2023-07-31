<script setup>

</script>
<template>
    <header class="header">
        <div class="header__container">
            <div class="header__logo"><a href="#"><span class="newcolor">A</span>Things</a></div>
            <div class="header__log">
                <div class="log-up">Log<span class="newcolor">Up</span></div>
                <div class="slash">|</div>
                <div class="log-in">Log<span class="newcolor">In</span></div>
            </div>
        </div>
    </header>
</template>
<style scoped lang="scss">
@import "../scss/variables.scss";
.header {
    width: 100%;
    height: 80px;
    position: fixed;
    z-index: 10;
    background-color: $colorGrey;
    &__container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        height: 80px;
        @extend %limiter;
    }
    &__logo {
        font-size: 48px;
    }
    &__log {
        display: flex;
        align-items: center ;
        *{
            font-size: 32px;
        }
        .slash{
            margin: 0px 10px;
        }
    }
    *{
        font-family: $fontES;
    }
}
.newcolor{
    color: $colorBlue;
}

</style>
