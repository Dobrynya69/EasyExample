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
</style>

                <!-- <div class="pagination">
                    <div @click="previousPage()" class="arrow">
                        <img src="../../public/arrow.png" class="arrow__img_l">
                    </div>
                    <div class="pagination__btns">
                        <button @click="gotoFirstPage()" class="pagination__btn" v-if="data.page != 1">1</button>

                        <button @click="previousPage()" class="pagination__btn" v-if="data.page - 1 > 1">{{ data.page - 1 }}</button>
                        <button class="small__btn pagination__btn active">{{ data.page  }}</button>
                        <button @click="nextPage()" class="pagination__btn" v-if="data.page + 1 < data.max_page">{{ data.page + 1 }}</button>
                        
                        <button @click="gotoLastPage()" class="pagination__btn" v-if="data.page != data.max_page">{{ data.max_page }}</button>
                    </div>
                    <div @click="nextPage()" class="arrow">
                        <img src="../../public/arrow.png" class="arrow__img_r">
                    </div>
                </div> -->