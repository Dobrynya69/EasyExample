<script setup>
defineProps(['modelValue'])
defineEmits(['update:modelValue'])
</script>
<template>
    <div class="filter__search_string">
        <input 
            type="text" 
            placeholder="Search..."
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target.value)"
        />
        <img src="../../public/loupe.png" alt="loupe"/>
    </div>
</template>
<style scoped lang="scss">
@import "../scss/variables.scss";
.filter{
    &__search_string {
        display: flex;
        align-items: center;
        background-color: $colorGrey;
        input{
            background-color: $colorGrey;
            font-family: $fontR;
            width: 100%;
            padding: 20px;
            padding-right: 0px;
            font-size: 20px;
        }
        input:focus{
            border: none;
            outline: none;
        }
        img{
            width: 60px;
            height: 60px;
        }
    }
}
</style>
