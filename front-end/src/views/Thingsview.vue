<script>
import { computed, mergeProps, ref } from 'vue';
import { useFetch } from '@vueuse/core';

var page = ref(1)

function myStart(){
    window.scroll({
        top: 0,
        left: 0,
    })
}

export default{
    async setup(){
        const  url = computed(() => {
            return `http://127.0.0.1:8000/api/anime/?string=&page=${page.value}`
        });
        const { isFetching, data } = await useFetch(url, {refetch: true}).json();
        return{
            data, isFetching
        }
    },
    methods:{
        nextPage(){
            if(page.value < this.data.max_page){
                myStart();
                page.value++;
            }
        },
        previousPage(){
            if(page.value > 1){
                myStart();
                page.value--;
            }
        },
        gotoFirstPage(){
            myStart();
            page.value = 1;
        },
        gotoLastPage(){
            myStart();
            page.value = this.data.max_page;
        },
    }
}
</script>
<template>
    <div class="main__container">
        <div class="main__filter">

        </div>
        <div class="main__content">
            <div class="content__items">
                <div class="content__item" v-for="item in data.results">
                    <div class="item__img">
                        <img :src="item.image" alt="image">
                    </div>
                    <div class="item__title">{{ item.title }}</div>
                </div>
            </div>
            <div class="pagination">
                <div @click="previousPage()" class="arrow">
                    <img src="../../public/arrow.png" class="arrow__img_l">
                </div>
                <div class="pagination__btns">
                    <button @click="gotoFirstPage()" class="pagination__btn" v-if="data.page != 1">1</button>

                    <button @click="previousPage()" class="pagination__btn" v-if="data.page - 1 > 1">{{ data.page - 1 }}</button>
                    <button class="small__btn pagination__btn active">{{ data.page }}</button>
                    <button @click="nextPage()" class="pagination__btn " v-if="data.page + 1 < data.max_page">{{ data.page + 1 }}</button>
                    
                    <button @click="gotoLastPage()" class="pagination__btn" v-if="data.page != data.max_page">{{ data.max_page }}</button>
                </div>
                <div @click="nextPage()" class="arrow rotate">
                    <img src="../../public/arrow.png" class="arrow__img_r">
                </div>
            </div>
        </div>
    </div>
</template>
<style>
.main__container {
    display: flex;
    min-height: calc(100vh - 80px);
    max-width: 1140px;
    margin: 0px auto;
}
.main__filter {
    width: 200px;
    padding: 20px;
    background-color: #49B0B7;
}
.main__content {
    width: calc(100% - 260px);
    padding: 20px;
    padding-right: 0px;
    background-color: rgba(19, 18, 18, 0.9);
}
.content__items {
    display: flex;
    flex-wrap: wrap;
}
.content__item {
    width: calc(25% - 20px);
    margin-bottom: 20px;
    margin-right: 20px;

}
.item__img {
    height: 300px;
    width: 100%;
}
.item__img img{
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.item__title {
    margin-top: 20px;
    color: #fff;
    font-family: 'Roboto', sans-serif;
    font-size: 18px;
}

.pagination {
    width: calc(100% - 20px);
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.arrow {
    width: 40px;
    height: 40px;
    background-color: #49B0B7;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
}
.arrow img{
    transition: transform 300ms;
    width: 20px;
    height: 20px;
}
.rotate{
    transform: rotate(180deg);
}
.pagination__btn {
    transition: background-color 300ms;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    border: none;
    margin: 0px 7.5px;
    background-color: #2C2C2C;
    color: #fff;
    font-size: 16px;
}
.active {
    background-color: #386568;

}
.arrow img:hover{
    transform: scale(1.3);
}
.pagination__btn:hover{
    cursor: pointer;
    background-color: #444444;
}
.arrow:hover{
    cursor: pointer;
}
.pagination__btn.active:hover{
    background-color: #386568;
    cursor: auto;
}
</style>
