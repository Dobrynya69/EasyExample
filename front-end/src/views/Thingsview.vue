<script>
import { computed, mergeProps, ref } from 'vue';
import { useFetch } from '@vueuse/core';

var page = ref(1)

export default{
    async setup(){
        const  url = computed(() => {
            return `http://127.0.0.1:8000/api/thing?string=&page=${page.value}`
        });
        const { isFetching, data } = await useFetch(url, {refetch: true}).json();
        return{
            data, isFetching
        }
    },
    methods:{
        nextPage(){
            page.value++;
            console.log(page.value);
        },
        previousPage(){
            page.value--;
            console.log(page.value);
        }
    }
}
</script>
<template>
    <div class="container">
        <div class="filter__menu">
            <div class="menu__title"><div>Filter</div></div>
            <div class="menu__content"></div>
        </div>
        <div class="container__items">
            <div class="items__title"><div class="item__text">List</div></div>
                <div class="container__row">
                    <div class="container__item" v-for="da in data.results">
                        <img :src="da.image" class="item__img" alt="" />
                        <div class="item__title"><div class="title__text">{{ da.title }}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
        <!-- <button class="ff" @click="previousPage()">ЖМИ ЕСЛИ НЕ МУЖИК</button>
        <button class="ff" @click="nextPage()">ЖМИ</button> -->
<style>
.filter__menu {
    min-width: 300px;
    height: 100vh;
    position: relative;
}
.menu__title div{
    font-family: 'Encode Sans SC', sans-serif;
}
.menu__title {

    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #a1a1a17c;
    color: #fff;
    font-size: 38px;
    padding: 10px 0px;
    position: absolute;
    left: 0;
    top: 0;
}
.menu__content {
    height: 100%;
    background-color: #545454;
}
.container{
    display: flex;
    
}
.items__title{
    width: 100%;
    background-color: #A1A1A1;
    padding: 10px 0px;
    font-size: 38px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.items__title div{
    font-family: 'Encode Sans SC', sans-serif;
}
.container__items{
    width: 100%;
    display: flex;
    align-items: center;
    flex-direction: column;
}
.container__row{
    display: flex;
    flex-wrap: wrap;

    margin: 10px auto;
    justify-content: start;
    
}
.container__item{
    width: 250px;
    height: 300px;
    position: relative;
    margin: 10px 50px;

}
.item__img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.item__title {
    width: calc(100% - 20px);
    min-height: 50px;
    padding: 10px;
    position: absolute;
    bottom: 0;
    left: 0;
    z-index: 10;
    background-color: #000000b0;
    color: #fff;
    display: flex;
    align-items: center;
}
.title__text{
    text-align: center;
    width: 100%;
    height: 100%;
}

</style>

