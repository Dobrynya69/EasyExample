<script setup>
import AnimeItem from './AnimeItem.vue';

const props = defineProps({
    data:{
        Type: Array
    }
});
</script>
<template>
    <div class="things__list">
        <AnimeItem :item="item" v-for="item in data" />
    </div>
</template>
<style scoped lang="scss">
@import "../scss/variables.scss";
.things {
    &__list{
        display: flex;
        flex-wrap: wrap;
        min-height: calc(100vh - 155px);
    }
}
</style>
