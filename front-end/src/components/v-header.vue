<script>
import { RouterLink } from 'vue-router'
export default{
    name:"v-header",
    data(){
        return{
            signActive: true,
        }
    },
    methods:{
        addActive(){
            this.signActive = !this.signActive
        }
    }
}
</script>
<template>
    <header class="header">
        <div class="header__content">
            <div ><router-link to="/" class="logo"  @click="this.signActive = true" ><span class="blue-letter">A</span>Things</router-link></div>
            <div class="sign" v-if="this.signActive">
                <div class="sign-up"><router-link to="/sign-up"  @click="addActive()">Sign<span class="blue-letter">Up</span></router-link></div>
                <div class="slash">|</div>
                <div class="sign-in"><router-link to="/sign-in" @click="addActive()">Sign<span class="blue-letter">In</span></router-link></div>
            </div>
        </div>
    </header>
</template>
<style>
.header{
    background-color: #2C2C2C;
    width: 100%;
    height: 80px;
    position: fixed;
    z-index: 10;
    top: 0;
    left: 0;
}
.header__content{
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 80px;
    max-width: calc(1140px - 40px);
    margin: 0 auto;
    padding: 0px 20px;
    color: #fff;
}
.blue-letter{
    color: #49B0B7;
}
.logo {
    font-family: 'Encode Sans SC', sans-serif;
    font-size: 40px;
}
.sign{
    display: flex;
    font-size: 24px;
}
.slash{
    margin: 0px 5px;
}

</style>


