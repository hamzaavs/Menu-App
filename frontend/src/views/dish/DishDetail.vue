<script setup>
import {onMounted} from "vue";
import {useRoute} from "vue-router";
import {useDishStore} from "@/store/dish.js";

const route = useRoute();
const dishStore = useDishStore();
const url = "http://127.0.0.1:8000"
onMounted(() => {
  dishStore.detail(route.params.unique_id);
});
</script>

<template>
  <div
    v-if="dishStore.dish"
    class="w-3/4 h-1/2 p-6 flex flex-row gap-10 shadow-md rounded-2xl bg-white justify-center items-center place-content-evenly hover:shadow-lg">
    <img :src="url+dishStore.dish.image" class="h-96 w-96 rounded-md " alt="">
    <div class="flex flex-col">
      <h1 class="text-center pt-20 text-3xl justify-self-center font-bold">{{ dishStore.dish.name }}</h1>
      <p class="text-center pt-16 text-2xl font-medium">{{ dishStore.dish.description }}</p>
      <div class="flex flex-col gap-8 pt-10">
        <p class=" text-lg"> Fiyat: {{ dishStore.dish.price }} ₺</p>
        <p
          v-if="dishStore.dish.stock > 15"
          class="w-44 rounded-md text-lg font-semibold text-center text-white px-4 py-3 bg-green-600">
          {{ dishStore.dish.stock }} Adet Kaldı
        </p>
        <p
          v-else-if="dishStore.dish.stock > 5"
          class="w-44 rounded-md text-lg font-semibold text-center text-white px-4 py-3 bg-yellow-600">
          {{ dishStore.dish.stock }} Adet Kaldı
        </p>
        <p
          v-else
          class="w-44 rounded-md text-lg font-semibold text-center text-white px-4 py-3 bg-red-600">
          {{ dishStore.dish.stock }} Adet Kaldı
        </p>
      </div>
      <button class="mb-14 text-2xl bg-blue-400 text-white w-48 h-20 mx-auto rounded-full">Sipariş Ver</button>
    </div>

  </div>

  <div v-else>
    <p>Yükleniyor...</p>
  </div>
</template>
