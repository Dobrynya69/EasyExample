<script>
import { RouterLink } from 'vue-router'
</script>
<template>
    <div class="sign__content">
        <div class="sign__btns">
            <router-link to="/sign-up"><button  class="sign-btn-active">SignUp</button></router-link>
            <router-link to="/sign-in"><button>SignIn</button></router-link>
        </div>
        <div class="form__content">
            <form class="sign-form" action="#">
                <div class="form__title">SignUp</div>
                <div class="form__data">
                    <div class="input__title">Email</div>
                    <input class="input" type="email">
                    <div class="input__title">Login</div>
                    <input class="input" type="text">
                    <div class="input__title">Password</div>
                    <input class="input" type="password">
                    <div class="input__title">Confirm Password</div>
                    <input class="input" type="password">
                    <br/>
                    <button class="done">SignUp</button>
                </div>
            </form>
        </div>
    </div>
</template>
<style>

</style>
