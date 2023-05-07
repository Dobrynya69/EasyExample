<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRouter, useRoute } from 'vue-router'
import Filter from '../components/v-filter.vue'
import SearchString from '../components/v-SearchString.vue';
import ItemsListItem from '../components/v-ItemsListItem.vue';
import api from '../api';

const router = useRouter()
const route = useRoute()
const anim = ref({});
const searchText = ref("");

onMounted(async () => {
    setDefaultImg()
    anim.value = await api.getAnime(null, searchText.value);
    searchText.value = route.query.searchString;
})
watch( searchText, async () =>{
    if(searchText.value !== undefined){
        anim.value = await api.getAnime(anim.page, searchText.value);
    }
});
const setPage = async (newPage) =>{
    if(newPage > 0 || newPage <= anim.max_page){
        myStart();
        setDefaultImg();
        anim.value = await api.getAnime(newPage, searchText.value);
    }
}
const handleChange = async (page) =>{
    router.push({query: { searchString: searchText.value }});

    anim.value = await api.getAnime(page, searchText.value);
}
const myStart = () =>{
    window.scroll({
        top: 0,
        left: 0,
        })
}
const setDefaultImg = () =>{
    const allImg = document.querySelectorAll(".anim__image")       
        for(let i = 0; i < allImg.length; i++){
            allImg[i].src = "../../public/load.png";
        }
}
</script>   
<template>
    <div class="main__container">
        <div class="main__filter">
            <SearchString @change="handleChange(anim.page)" v-model="searchText"/>
            <div class="filter__content">
                <Filter />
            </div>
        </div>
        <div class="main__content">
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
        </div>
    </div>
</template>
<style>
.loading{
    font-size: 50px;
    background-color: #2C2C2C;
    color: #fff;
}
.main__container {
    display: flex;
    min-height: calc(100vh - 80px);
    max-width: 1140px;
    margin: 0px auto;
}
.main__filter {
    width: 250px;
    background-color: #49B0B7;
}
.filter__content{
    padding: 20px;
}
::-webkit-input-placeholder {
    color:#fff;
}
.main__content {
    width: calc(100% - 260px);
    padding: 20px;
    padding-right: 0px;
    background-color: rgba(19, 18, 18, 0.9);
}

</style>
