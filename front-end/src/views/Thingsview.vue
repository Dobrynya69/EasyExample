<script setup>
import { computed, onServerPrefetch, ref, onMounted } from 'vue';
import {useRoute, RouterView} from 'vue-router'
import Filter from '../components/v-filter.vue'
import ItemsList from '../components/v-ItemsList.vue'
import SearchString from '../components/v-SearchString.vue';
</script>   
<template>
    <div class="main__container">
        <div class="main__filter">
            <SearchString/>
            <div class="filter__content">
                <Filter />
            </div>
        </div>
        <div class="main__content">
            <Suspense>
                <template #default>
                    <ItemsList/>
                </template>
                <template #fallback>
                    Loading....
                </template>
            </Suspense>
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
