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
        <div ><router-link to="/" class="logo"  @click="this.signActive = true" >AThings</router-link></div>
        <div class="sign" v-if="this.signActive">
            <div class="sign-up"><router-link to="/sign-up"  @click="addActive()">SignUp</router-link></div>
            <div class="slash">|</div>
            <div class="sign-in"><router-link to="/sign-in" @click="addActive()">SignIn</router-link></div>
        </div>
    </div>
</header>
</template>
<style>
.header{
    background-color: #d9d9d9d8;
    width: 100%;
    height: 80px;
    position: fixed;
    z-index: 100;
    top: 0;
    left: 0;
}
.header__content{
    display: flex;
    align-items: center;
    justify-content: space-between;
    
    height: 80px;
    max-width: calc(1770px - 20px);
    padding: 0px 10px;
    margin: 0px auto;
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


