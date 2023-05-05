<script setup>


</script>
<template>

</template>
<style>
.content__items {
    display: flex;
    flex-wrap: wrap;
}
.pagination {
    width: calc(100% - 20px);
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.arrow {
    width: 40px;
    height: 40px;
    background-color: #49B0B7;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
}
.arrow img{
    transition: transform 300ms;
    width: 20px;
    height: 20px;
}
.rotate{
    transform: rotate(180deg);
}
.pagination__btns{
    display: flex;

}
.pagination__btn {
    transition: background-color 300ms;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    border: none;
    margin: 0px 7.5px;
    background-color: #2C2C2C;
    color: #fff;
    font-size: 16px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.active {
    background-color: #386568;

}
.arrow img:hover{
    transform: scale(1.3);
}
.pagination__btn:hover{
    cursor: pointer;
    background-color: #444444;
}
.arrow:hover{
    cursor: pointer;
}
.pagination__btn.active:hover{
    background-color: #386568;
    cursor: auto;
}
</style>
