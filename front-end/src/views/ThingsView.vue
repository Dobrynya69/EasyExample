<script setup>
import VHeader from '../components/htmlComponents/VHeader.vue';
import VFooter from '../components/htmlComponents/VFooter.vue';
import VMain from '../components/htmlComponents/VMain.vue';
import AnimeList from '../components/AnimeList.vue';
import api from "../api"
import {onMounted, ref} from 'vue'
import { useRouter, useRoute } from 'vue-router'

const route = useRoute();
const router = useRouter();

const anime = ref({});

onMounted(async () =>{
    setDefaultImg();
    console.log(route.query.page)
    if(route.query.page == 1){
        router.push("/")
        anime.value = await api.getAnime();
    }
    else{
        anime.value = await api.getAnime(route.query.page);
    }
    console.log(anime.value);
});

const setPage = async (page) => {
    if(page >= 1 && page <= anime.value.max_page){
        page_up();
        setDefaultImg();
        router.push({query: { page: page }});
        anime.value = await api.getAnime(page);
    }

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
                <div class="filter__search_string">
                    <input type="text" placeholder="Search..."/>
                    <img src="../../public/loupe.png" alt="loupe"/>
                </div>
                <div class="filter__container">
                    <div class="filter__reset_btn"><button>Reset</button></div>
                    <div class="filter__list">
                        
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
    &__search_string {
        display: flex;
        background-color: $colorGrey;
        input{
            background-color: $colorGrey;
            font-family: $fontR;
            width: 100%;
            padding: 20px;
            padding-right: 0px;
            font-size: 20px;
        }
        input:focus{
            border: none;
        outline: none;
        }
    }
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
        }
    }
    &__list {

    }
    &__sort_btn {
        width: 100%;

        button{
            width: 100%;
            font-family: $fontES;
            background-color: $colorGrey;
            font-size: 24px;
            padding: 10px 0px;
        }
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
