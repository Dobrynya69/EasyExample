<script setup>
import { RouterLink, RouterView } from 'vue-router'
import vHeader from './components/v-header.vue';
import vFooter from './components/v-footer.vue';
import Thingsview from './views/Thingsview.vue';

</script>

<template>
    <div class="background">
        <img src="../public/bg.png" alt="">
        <div class="img__color"></div>
    </div>
    <vHeader/>
        <div class="main">
            <Suspense>
                <template #default>
                    <RouterView/>
                </template>
                <template #fallback>
                    <div class="gg">Loading..</div>
                </template>
            </Suspense>
        </div>
    <vFooter/>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Encode+Sans+SC&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
*{
    margin: 0;
    padding: 0;
    list-style: none;
    text-decoration: none;
    font-family: 'Roboto', sans-serif;
}
::-webkit-scrollbar{
    width: 10px;
}
::-webkit-scrollbar-track{
    background: #131212;
}
::-webkit-scrollbar-thumb{
    background: linear-gradient(#49B0B7, #39898f);
    border: 4px solid #131212;
    border-radius: 5px;
    transition: 300ms;
}
a { color: inherit; } 
.background{
    width: 100%;
    height: 100%;
}
.img__color{
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.4);
    position: absolute;
    z-index: 2;
}
.background img{
    position: absolute;
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
    z-index: 1;
}
.main{
    max-width: 1920px;
    margin: 0px auto;
    min-height: calc(100vh - 80px);
    padding-top: 80px;
}
</style>
