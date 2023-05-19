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
            <div class="black-some"><img class="some-img" src="../../public/info.png" alt="lupa"></div>
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
.black-some {
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.8);
    position: absolute;
    opacity: 0;
    transition: all 300ms;
}
.black-some > *{
    position: absolute;
    transition: all 300ms;
    left: 50%;
    top: 50%;
    transform: scale(0) translate(-50%, -50%);
}
.black-some:hover {
    opacity: 1;
}
.black-some:hover .some-img{
    transform: scale(1)  translate(-50%, -50%);
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
@media (max-width: 1025px) {
    .content__item{
        width: calc(25% - 10px);
        margin-right: 10px;
    }
}
@media (max-width: 941px) {
    .content__item{
        width: calc(33% - 10px);
        margin-bottom: 10px;
        margin-right: 10px;
    }
}
@media (max-width: 741px) {
    .content__item{
        width: calc(50% - 10px);
        margin-bottom: 10px;
        margin-right: 10px;
    }
}
</style>