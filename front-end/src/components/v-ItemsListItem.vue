<script setup>
const props = defineProps({
    item: {
        required: true,
        type: Object
    },
})
</script>

<template>
    <div class="content__item" >
        <div class="item__img">
            <img class="anim__image" :src="item.image" alt="image">
        </div>
        <div class="item__title">{{ item.title }}</div>
    </div>
</template>
<style scoped>
.content__item {
    width: calc(25% - 20px);
    margin-bottom: 20px;
    margin-right: 20px;
}
.item__img {
    height: 300px;
    width: 100%;
    position: relative;
}
.anim__image{
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
</style>