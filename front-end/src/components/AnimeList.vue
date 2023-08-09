<script setup>
import api from "../api"
import {onMounted, ref} from 'vue'

const anime = ref({});

onMounted(async () =>{
    anime.value = await api.getAnime();
    console.log(anime.value.results[0].title);
});


</script>
<template>
    <div class="things">
        <div class="things__filter"></div>
        <div class="things__content">
            <div class="things__list">
                <div class="things__item" v-for="item in anime.results">
                    <div class="item__img">
                        <img src="../../public/bg.png" alt="item_img">
                    </div>
                    <div class="item__title">Lorem ipsum dolor sit amet consectetur.</div>
                </div>
            </div>
        </div>
    </div>
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
        width: 20%;
        background-color: $colorBlue;
        padding: 20px;
    }
    &__content {
        width: 100%;
        background-color: $colorBlackA;
        padding: 0px 10px;
        padding-top: 20px;

    }
    &__list{
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: center;
    }
    &__item{
        max-width: calc(25% - 20px);
        padding: 20px 10px;
        padding-top: 0px;
    }
}
.item{
    &__img{
        width: 100%;
        height: 300px;
        margin-bottom: 10px;
        img{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
    }
    &__title{

    }
}

</style>
