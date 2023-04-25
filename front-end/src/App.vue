<script setup>
import { RouterLink, RouterView } from 'vue-router'
import vHeader from './components/v-header.vue';
import vFooter from './components/v-footer.vue';
import Thingsview from './views/Thingsview.vue';

</script>

<template >
    <vHeader/>
    <div class="content">
        <Suspense>
            <template #default>
                <RouterView/>
            </template>
            <template #fallback>
                <div class="gg">Loading..</div>
            </template>
        </Suspense>
    </div>
    <vFooter/>

</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Encode+Sans+SC&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
*{
    margin: 0;
    padding: 0;
    list-style: none;
    text-decoration: none;
    font-family: 'Roboto', sans-serif;
}
a { color: inherit; } 
.content{
    min-height: calc(100vh - 80px);
    padding-top: 80px;
}
</style>
