<script setup>

</script>
<template>
    <div class="search">
        <input id="searchString" type="text" placeholder="Search...">
        <img src="../../public/lupa.png" alt="lupa">
    </div>
</template>
<style>
.search {
    width: calc(100% - 2px);
    height: 55px;
    display: flex;
    background-color: #2C2C2C;
    border: solid 1px #49B0B7;
}
.search input{
    font-family: 'Roboto', sans-serif;
    width: calc(100% - 20px);
    background-color: #2C2C2C;
    border: none;
    padding: 20px;
    padding-right: 0px;
    font-size: 20px;
    color:#fff;
}
.search input:focus{
    border: none;
    outline: none;
}
</style>

