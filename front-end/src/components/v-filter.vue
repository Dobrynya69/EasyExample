<script setup>
import { useFetch } from '@vueuse/core';
import { computed, mergeProps, ref, onMounted } from 'vue';
import api from '../api';

const genresList = ref({});

onMounted(async () => {
    genresList.value = await api.getGenres();
})
</script>
<template>
    <form action="#" class="filter__form">
        <div class="geners__list">
            <div class="checkbox__block" v-for="item in genresList.genres">
                <label class="block__label">
                    <div class="label__text">{{ item.name }}</div> 
                    <input type="checkbox">
                </label>
            </div>
        </div>
        <button class="sort__btn">Sort</button>
    </form>
</template>
<style>
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

    font-size: 24px;
    font-family: 'Encode Sans SC', sans-serif;
    background-color: #2C2C2C;
    color: #fff;
    padding: 12px 0px;
    border: none;
}
</style>
