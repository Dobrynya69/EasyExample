<script>
import { computed, mergeProps, ref } from 'vue';
import { useFetch } from '@vueuse/core';

var page = ref(1)

export default{
    async setup(){
        const  url = computed(() => {
            return `http://127.0.0.1:8000/api/thing?string=&page=${page.value}`
        });
        const { data } = await useFetch(url, {refetch: true}).json();
        return{
            data,
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
        <div class="container__row" >
            <div class="container__item" v-for="da in data.results">
                <img :src="da.image" class="item__img" alt="" />
                <div class="item__title">{{ da.title }}</div>
                <div class="item__year">{{ da.year }}</div>
            </div>
        </div>
        <button class="ff" @click="previousPage()">ЖМИ ЕСЛИ НЕ МУЖИК</button>
        <button class="ff" @click="nextPage()">ЖМИ</button>
    </div>
</template>
<style>
.container__row{
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    padding: 10px 0px;
}
.container__item{
    background-color: #0e0e0e;
    color: #fff;
    width: 300px;
    text-align: center;
    padding: 10px;
    margin-bottom: 10px;
    font-size: 20px;
}
.item__img{
    height: 400px;
    max-width: 100%;
    object-fit: cover;
}
</style>

