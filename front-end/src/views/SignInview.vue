<script>
import { RouterLink } from 'vue-router'
</script>
<template>
    <div class="sign__content">
        <div class="sign__btns">
            <router-link to="/sign-up"><button>SignUp</button></router-link>
            <router-link to="/sign-in"><button class="sign-btn-active">SignIn</button></router-link>
        </div>
        <div class="form__content">
            <form class="sign-form" action="#">
                <div class="form__title">SignIn</div>
                <div class="form__data">
                    <div class="input__title">Login</div>
                    <input class="input" type="text">
                    <div  class="input__title">Password</div>
                    <input class="input" type="password">
                    <br/>
                    <button class="done">SignIn</button>
                </div>
            </form>
        </div>
    </div>
</template>
<style>
.sign__content{
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.form__content{
    width: calc(100% - 10px);
    padding: 10px 5px;
    min-height: calc(100vh - 180px);
    display: flex;
    justify-content: center;
    align-items: center;
}
.sign-form{
    max-width: 900px;
    min-width: 300px;
    width: 100%;
    background-color: #545454;
}
.form__title{
    height: 69px;
    background-color: #D9D9D9;
    font-size: 40px;
    text-align: center;
    font-family: 'Encode Sans SC', sans-serif;
}
.form__data {
    width: calc(100% - 100px);
    margin: 50px;
    font-family: 'Encode Sans SC', sans-serif;
}
.input__title {
    font-family: 'Encode Sans SC', sans-serif;
    font-size: 24px;
    color: #fff;
}
.input {
    font-family: 'Encode Sans SC', sans-serif;
    font-size: 35px;
    background-color: #E6E6E6;
    padding: 5px 5px;
    width: calc(100% - 10px);
    border: none;
    margin-bottom: 35px;
}
input:focus{
    outline: none;
}
.done{
    font-family: 'Encode Sans SC', sans-serif;
    width: 100%;
    height: 54px;
    border: none;
    background-color: #A1A1A1;
    color: black;
    font-size: 35px;
}
.done:hover{
    cursor: pointer;
}
.sign__btns{
    width: 100%;
}
.sign__btns button{
    width: 50%;
    height: 80px;
    border: none;
    background-color: #A1A1A1;
    font-size: 40px;
}
.sign__btns button:hover{
    cursor: pointer;
}
.sign__btns button.sign-btn-active{
    background-color: #545454;
    color: #fff;
}
</style>