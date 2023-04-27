<script>
import { computed, mergeProps, ref } from 'vue';
import { useFetch } from '@vueuse/core';

var page = ref(1)

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
                page.value++;
            }
        },
        previousPage(){
            if(page.value > 1){
                page.value--;
            }
        },
        gotoFirstPage(){
            page.value = 1;
        },
        gotoLastPage(){
            page.value = this.data.max_page;
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
                <div class="container__row">
                    <div class="container__item" v-for="da in data.results">
                        <img :src="da.image" class="item__img" alt="" />
                        <div class="item__title"><div class="title__text">{{ da.title }}</div>
                    </div>
                </div>
                <div class="pagination">
                    <div @click="previousPage()" class="arrow">
                        <img src="../../public/arrow.png" class="arrow__img_l">
                    </div>
                    <div class="pagination__btns">
                        <button @click="gotoFirstPage()" class="pagination__btn" v-if="data.page != 1">1</button>
                        
                        <!-- page.value > 1 -->
                        <!-- page.value < (max_page - 1) -->
                        <!-- data.page != page.max_page -->

                        <button @click="previousPage()" class="pagination__btn" v-if="data.page - 1 > 1">{{ data.page - 1 }}</button>
                        <button class="small__btn pagination__btn active">{{ data.page  }}</button>
                        <button @click="nextPage()" class="pagination__btn" v-if="data.page + 1 < data.max_page">{{ data.page + 1 }}</button>
                        
                        <button @click="gotoLastPage()" class="pagination__btn" v-if="data.page != data.max_page">{{ data.max_page }}</button>
                    </div>
                    <div @click="nextPage()" class="arrow">
                        <img src="../../public/arrow.png" class="arrow__img_r">
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<style>
.pagination {
    width: 100%;
    padding: 0px 90px;
    margin-top: 50px;
    margin-bottom: 30px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.arrow__img_l {
    width: 20px;
    height: 20px;
}
.arrow__img_r {
    width: 20px;
    height: 20px;
    transform: rotate(180deg);
}
.arrow{
    display: flex;
    justify-content: center;
    align-items: center;

    width: 40px;
    height: 40px;
    background-color: #545454;
    border-radius: 50%;
}
.arrow:hover{
    cursor: pointer;
}
.pagination__btn {
    font-size: 20px;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    border: none;
    background-color: #54545494;
    color: #fff;
    margin: 0px 5px;
}
.pagination__btn:hover{
    cursor: pointer;
}
.pagination__btn.active{
    background-color: #545454
}
.filter__menu {
    min-width: 300px;
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
    min-height: 100vh;
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
    display: flex;
    align-items: center;
    flex-direction: column;
}
.container__row{
    display: flex;
    flex-wrap: wrap;
    margin: 10px auto;
    justify-content: center;
}
.container__item{
    width: 250px;
    height: 320px;
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

