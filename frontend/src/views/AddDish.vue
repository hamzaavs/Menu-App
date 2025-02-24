<script setup>
import {reactive} from "vue";
import {useAuthStore} from "@/store/auth.js";
import api from "@/api/axios.js";

const authStore = useAuthStore();
const dish = reactive({
  name: '',
  description: '',
  price: 0.0,
  stock: 0
});

const addDish = async () => {
  try {
    return api.post('/dishes/', dish)
  } catch (err) {
    console.log(err)
  }
}

</script>

<template>
<div class="w-1/2" v-if='authStore.isAdmin'>
    <h1 class="text-2xl font-bold text-center my-16" >Yemek Ekle</h1>
    <form @submit.prevent="addDish" class="flex flex-col gap-10">
      <input class="rounded-md p-3" v-model="dish.name" type="text" placeholder="Yemek Adı">
      <input class="rounded-md p-3" v-model="dish.description" type="text" placeholder="Açıklama">
      <input class="rounded-md p-3" v-model="dish.price" type="number" placeholder="Fiyat">
      <input class="rounded-md p-3" v-model="dish.stock" type="number" placeholder="Stok">

      <button type="submit" class="w-28 m-auto bg-white border-solid border border-gray-400 rounded-md">Yemek Ekle
      </button>
    </form>
  </div>
  <div class="w-1/2" v-else>
    <p>Bu sayfaya erişim yetkiniz yok.</p>
  </div>
</template>
