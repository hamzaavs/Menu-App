<script setup>
import {onMounted} from "vue";
import {useDishStore} from "@/store/dish.js";

const dishStore = useDishStore()
const url = "http://127.0.0.1:8000/"

onMounted(() => {
  dishStore.list()
})

</script>


<template>
  <div class="w-3/5 grid grid-cols-3 gap-10 mt-28 ease-in ">
    <div
      v-for="item in dishStore.dishes"
      :key="item.name"
      class="text-center bg-white p-10 shadow-lg rounded-md duration-300 hover:translate-y-[-15px]"
    >
      <img :src="url+item.image" alt="Yemek Resmi" class="rounded-full mb-5 "/>
      <h1 class="text-title text-2xl font-bold mb-2">{{ item.name }}</h1>
      <p class="text-price text-lg mb-10">{{ item.price }}₺</p>
      <router-link :to="`/dish/${item.id}`" class="bg-primary text-black p-2 m rounded-md">İncele</router-link>
    </div>
  </div>
</template>

