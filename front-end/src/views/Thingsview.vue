<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRouter, useRoute } from 'vue-router'
import SearchString from '../components/v-SearchString.vue';
import ItemsListItem from '../components/v-ItemsListItem.vue';
import api from '../api';

const router = useRouter()
const route = useRoute()

const anim = ref({});
const genresList = ref({});
const filterList = ref([]);
const searchText = ref("");

onMounted(async () => {
    // setDefaultImg()
    anim.value = await api.getAnime(null, searchText.value);
    genresList.value = await api.getGenres();
    searchText.value = route.query.searchString;
})
watch( searchText, async () =>{
    if(searchText.value !== undefined){
        anim.value = await api.getAnime(anim.page, searchText.value);
    }
});
const setPage = async (newPage) =>{
    if(filterList.value.length > 0){
        if(newPage > 0 || newPage <= anim.max_page){
            myStart();
            setDefaultImg();
            anim.value = await api.getAnimeWithGenres(filterList.value, newPage, searchText.value);
        }
    }
    else{
        if(newPage > 0 || newPage <= anim.max_page){
            myStart();
            setDefaultImg();
            anim.value = await api.getAnime(newPage, searchText.value);
        }
    }
}
const filterData = async () => {
    if(filterList.value.length > 0){
        myStart();
        // setDefaultImg();
        anim.value = await api.getAnimeWithGenres(filterList.value, 1, searchText.value);
    }
}
const handleChange = async (page) =>{
    router.push({query: { searchString: searchText.value }});
    if(filterList.value.length > 0){
        anim.value = await api.getAnimeWithGenres(filterList.value, 1, searchText.value);
    }
    else{
        anim.value = await api.getAnime(page, searchText.value);
    }
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
                <form  class="filter__form" @submit.prevent>
                    <button @click="" class="reset__btn">Reset</button>
                    <div class="geners__list">
                        <div class="checkbox__block" v-for="item in genresList.genres">
                            <label class="block__label">
                                <div class="label__text">{{ item.name }}</div> 
                                <input
                                :value="item.name"
                                type="checkbox"
                                v-model="filterList"
                                >
                            </label>
                        </div>
                    </div>
                    <button @click="filterData()" class="sort__btn">Sort</button>
                </form>
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
.cal{
    color: #fff;
    font-size: 24px;
}
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

input[type="checkbox"] {
    -webkit-appearance: none;
    appearance: none;
    margin: 0;
    width: 20px;
    height: 20px;
    background-color: #4D4D4D;

    display: grid;
    place-content: center;
    transition: 120ms transform ease-in-out;
}
input[type="checkbox"]:checked {
    background-color: #49B0B7;
}
.label__text{
    margin-right: 10px;
    overflow: auto;
}
.geners__list{
    background-color: #2C2C2C;
    max-height: 458px;
    overflow: auto;
    padding: 20px;
}
.checkbox__block{
    margin-bottom: 10px;
}
.block__label{
    font-size: 20px;
    color: #fff;
    display: grid;
    grid-template-columns: 1fr 20px;
    align-items: center;
}
.sort__btn{
    width: 100%;
    margin-top: 20px;
    transition: all 300ms;

    font-size: 24px;
    font-family: 'Encode Sans SC', sans-serif;
    color: #fff;
    padding: 10px 0px;
    background-color: #2C2C2C;
    border: 1px solid #2C2C2C;
}
.sort__btn:hover{
    cursor: pointer;
    background-color: #49B0B7;
    border: 1px solid #2C2C2C;
    color: #000;
}
.reset__btn{
    width: 100%;
    margin-bottom: 20px;
    transition: all 300ms;
    font-size: 24px;
    padding: 10px 0px;
    font-family: 'Encode Sans SC', sans-serif;
    background-color: #49B0B7;
    border: 1px solid #2C2C2C;

}
.reset__btn:hover{
    cursor: pointer;
    background-color: #2C2C2C;
    border: 1px solid #2C2C2C;
    color: #fff;
}
</style>
