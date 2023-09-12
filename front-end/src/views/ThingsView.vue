<script setup>
import VHeader from '../components/htmlComponents/VHeader.vue';
import VFooter from '../components/htmlComponents/VFooter.vue';
import VMain from '../components/htmlComponents/VMain.vue';
import AnimeList from '../components/AnimeList.vue';
import SearchString from '../components/SearchString.vue'
import api from "../api"
import {onMounted, ref, onBeforeMount} from 'vue'
import { useRouter, useRoute } from 'vue-router'

const route = useRoute();
const router = useRouter();

const anime = ref({});
const genres = ref({})

const searchString = ref("");


onMounted(async () =>{
    genres.value = await api.getGenre();
    anime.value = await api.getAnime(route.query.page);
    if(route.query.searchString !== ""){
        searchString.value = route.query.searchString;
        anime.value = await api.getAnimeWithSearchString(route.query.page, route.query.searchString);
    }

});

const setPage = async (page) => {
    if(page >= 1 && page <= anime.value.max_page){
        page_up();
        setDefaultImg();
        router.push({query: { page: page, searchString: searchString.value }});
        if(searchString.value !== ""){
            anime.value = await api.getAnimeWithSearchString(page, route.query.searchString);
        }
        else{
            anime.value = await api.getAnime(page);
        }
    }
}
const setAnimeWithGenre = async (page) => {
    router.push({query: { page: route.query.page, searchString: searchString.value }});
    // if(filterList.value.length > 0){
    //     anime.value = await api.getAnimeWithGenres(filterList.value, 1, searchText.value);
    // }
    // else{
    //     anime.value = await api.getAnime(page, searchText.value);
    // }
    anime.value = await api.getAnimeWithSearchString(page, searchString.value);
}
const page_up = () =>{
    window.scroll({
        top: 0,
        left: 0,
    })
}
const setDefaultImg = () =>{
    const allImg = document.querySelectorAll(".item__img_img")       
    for(let i = 0; i < allImg.length; i++){
        allImg[i].src = "../../public/bg.png";
    }
}
</script>
<template>
    <VHeader/>
    <VMain>
        <div class="things">
            <div class="things__filter">
                <SearchString
                    @change="setAnimeWithGenre(anime.page)" 
                    v-model="searchString"
                />
                <div class="filter__container">
                    <div class="filter__reset_btn"><button>Reset</button></div>
                    <div class="filter__genres">
                        <div class="genres__list">
                            <div class="genres__item" v-for="item in genres.genres"><span>{{ item.name }}</span><input type="checkbox"/></div>
                        </div>
                    </div>
                    <div class="filter__sort_btn"><button>Sort</button></div>
                </div>
            </div>
            <div class="things__content">
                <AnimeList :data="anime.results"/>
                <div class="things__pagination">
                    <div @click="setPage(anime.page - 1)" class="pagination__arrow"><img src="../../public/arrow_left.png" alt="arrow"></div>
                    <div class="pagination__btns">
                        <div @click="setPage(1)" class="pagination__btn" v-if="anime.page != 1" ><button>1</button></div>
                        <div @click="setPage(anime.page - 1)" class="pagination__btn active__btn" v-if="anime.page - 1 > 1"><button>{{ anime.page - 1 }}</button></div>
                        <div class="pagination__btn"><button>{{ anime.page }}</button></div>
                        <div @click="setPage(anime.page + 1)" class="pagination__btn active__btn" v-if="anime.page + 1 < anime.max_page"><button>{{ anime.page + 1 }}</button></div>
                        <div @click="setPage(anime.max_page)" class="pagination__btn" v-if="anime.page != anime.max_page"><button>{{ anime.max_page }}</button></div>
                    </div>
                    <div @click="setPage(anime.page + 1)" class="pagination__arrow"><img src="../../public/arrow_right.png" alt="arrow"></div>
                </div>
            </div>
        </div>
    </VMain>
    <VFooter/>
</template>

<style scoped lang="scss">
@import "../scss/variables.scss";
.things {
    width: 100%;
    position: relative;
    display: flex;
    z-index: 2;
    padding-top: 80px;
    &__filter {
        width: calc(30% - 2px);
        background-color: $colorBlue;
        border: 1px $colorBlue solid;
    }
    &__content {
        width: 100%;
        background-color: $colorBlackA;
        padding: 0px 10px;
        padding-top: 20px;
    }
    &__pagination {
        display: flex;
        justify-content: space-between;
        align-items: centers;
        margin: 10px 0px;
    }
}
.filter {
    &__container {
        padding: 20px;
    }
    &__reset_btn {
        width: 100%;
        button{
            width: 100%;
            font-family: $fontES;
            background-color: $colorBlue;
            border: 1px $colorGrey solid;
            font-size: 24px;
            padding: 10px 0px;
            color: $colorGrey;
            transition: all 300ms;
        }
        button:hover{
            cursor: pointer;
            width: 100%;
            font-family: $fontES;
            background-color: $colorGrey;
            font-size: 24px;
            padding: 10px 0px;
            color: #fff;
        }
    }
    &__genres {
        max-height: 500px;
        margin: 20px 0px;
        overflow-y: scroll;
        background-color: $colorGrey;
        padding: 20px;
    }
    &__sort_btn {
        width: 100%;
        button{
            width: 100%;
            font-family: $fontES;
            background-color: $colorGrey;
            font-size: 24px;
            padding: 10px 0px;
            transition: all 300ms;
        }
        button:hover{
            cursor: pointer;
            width: 100%;
            font-family: $fontES;
            background-color: $colorBlue;
            border: 1px $colorGrey solid;
            font-size: 24px;
            padding: 10px 0px;
            color: $colorGrey;
        }
    }
}
.genres {
    &__list {

    }
    &__item {
        font-size: 20px;
        font-family: $fontR;
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
        border-bottom: 3px solid $colorGrey2;
        padding-bottom: 3px;
        input[type="checkbox"] {
            -webkit-appearance: none;
            appearance: none;
            margin: 0;
            width: 20px;
            height: 20px;
            background-color: $colorGrey2;
            display: grid;
            place-content: center;
            cursor: pointer;
            transition: 120ms transform ease-in-out;
        }
        input[type="checkbox"]:checked {
            background-color: $colorBlue;
        }
    }
    &__item:last-child{
        margin-bottom: 0px;
    }
}


.pagination {
    &__arrow {
        width: 40px;
        height: 40px;
        background-color: $colorBlue;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        img{
            width: 20px;
            height: 20px;
        }
    }
    &__btns {
        display: flex;
        align-items: center;
    }
    &__btn {
        margin: 0px 7.5px;
        width: 30px;
        height: 30px;
        button{
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background-color: $colorBtns;
        }
    }
}
.active__btn{
    button{
        background-color: $colorGrey;
    }
}

</style>
