<script setup>
import { RouterLink, RouterView } from 'vue-router'
import vHeader from './components/v-header.vue';
import vFooter from './components/v-footer.vue';
import Thingsview from './views/Thingsview.vue';

</script>

<template>
    <vHeader/>
        <div class="main">
            <RouterView/>
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
.main{
    position: relative;
    z-index: 3;
    padding-top: 80px;
}
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
    object-fit: cover;
    position: absolute;
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
    z-index: 1;
}
body{
    position: relative;
}
</style>
