<script setup>
import ItemsListItem from './v-ItemsListItem.vue';
import { defineProps, ref, onMounted } from 'vue'
import {useRoute} from 'vue-router'
import api from '../api';


const anim = ref({});
onMounted(async () => {
    anim.value = await api.getAnime(null);
})
async function setPage(newPage){
    if(newPage > 0 || newPage <= anim.max_page){
        const props = {page: newPage}
        console.log(props)
        anim.value = await api.getAnime(props);
    }
}

</script>
<template>
    <div class="content__items">
        <ItemsListItem 
        v-for="item in anim.results" 
        :item="item" 
    />
    </div>
    <div class="pagination">
        <div @click="setPage(anim.page - 1)" class="arrow">
            <img src="../../public/arrow.png" class="arrow__img_l">
        </div>
        <div class="pagination__btns">
            <div @click="setPage(1)"  class="pagination__btn" v-if="anim.page != 1">1</div>

            <div @click="setPage(anim.page - 1)" class="pagination__btn" v-if="anim.page - 1 > 1">{{ anim.page - 1 }}</div>
            <div class="small__btn pagination__btn active">{{ anim.page }}</div>
            <div @click="setPage(anim.page + 1)" class="pagination__btn " v-if="anim.page + 1 < anim.max_page">{{ anim.page + 1 }}</div>
            
            <div @click="setPage(anim.max_page)" class="pagination__btn" v-if="anim.page != anim.max_page">{{ anim.max_page }}</div>
        </div>
        <div @click="setPage(anim.page + 1)" class="arrow rotate">
            <img src="../../public/arrow.png" class="arrow__img_r">
        </div>
    </div>
</template>
<style>
.content__items {
    display: flex;
    flex-wrap: wrap;
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
.pagination__btns{
    display: flex;

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
    display: flex;
    justify-content: center;
    align-items: center;
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
