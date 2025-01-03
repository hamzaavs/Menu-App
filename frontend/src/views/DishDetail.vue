<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const id = route.params.id;

const dish = ref({});

const getDishDetail = async () => {
  await axios.get(`http://127.0.0.1:8000/dishes/${id}`)
    .then((res) => {
      dish.value = res.data;
    });
};

onMounted(() => {
  getDishDetail();
});
</script>

<template>
  <div class="w-3/4 h-1/2 p-6 flex flex-col shadow-md rounded-2xl bg-white justify-center place-content-evenly hover:shadow-lg">
    <h1 class="text-center pt-20 text-3xl justify-self-center font-bold">{{ dish.name }}</h1>
    <p class="text-center pt-16 text-2xl font-medium">{{ dish.description }}</p>
    <div class="flex flex-col gap-8 pt-10">
      <p class=" text-lg"> Fiyat: {{ dish.price }} ₺</p>
      <p
        v-if="dish.stock > 15"
        class="w-44 rounded-md text-lg font-semibold text-center text-white px-4 py-3 bg-green-600">
          {{dish.stock}} Adet Kaldı
      </p>
      <p
        v-else-if="dish.stock > 5 || dish.stock < 15"
        class="w-44 rounded-md text-lg font-semibold text-center text-white px-4 py-3 bg-yellow-600">
          {{dish.stock}} Adet Kaldı
      </p>
      <p
        v-else
        class="w-44 rounded-md text-lg font-semibold text-center text-white px-4 py-3 bg-red-600">
          {{dish.stock}} Adet Kaldı
      </p>
    </div>
    <button class="mb-14 text-2xl bg-blue-400 text-white w-48 h-20 mx-auto rounded-fulln dev">Sipariş Ver</button>
  </div>
</template>
