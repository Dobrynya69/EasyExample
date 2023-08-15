<script setup>

const props = defineProps({
    item:{
        Type: Object
    }
})

</script>
<template>
    <div class="things__item">
        <div class="item__img">
            <img :src="item.image" alt="item_img" class="item__img_img">
        </div>
        <div class="item__title">{{ item.title }}</div>
    </div>
</template>
<style scoped lang="scss">
@import "../scss/variables.scss";
.things {
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
        font-size: 20px;
        font-family: $fontR;
    }
}
</style>
