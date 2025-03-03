<script setup>
import {nextTick, reactive} from "vue";
import {useAuthStore} from "@/store/auth.js";
import {useDishStore} from "@/store/dish.js";
import router from "@/router/index.js";

const authStore = useAuthStore();
const dishStore = useDishStore();

const dish = reactive({
  name: '',
  description: '',
  price: 0.0,
  stock: 0,
  selectedImage: null
});

const handleImageChange = (event) => {
  dish.selectedImage = event.target.files[0]
}

const addDish = async () => {
  try {
    if (!dish.selectedImage) {
      alert("Dosya seçiniz")
    }

    await dishStore.create(dish.name, dish.description, dish.price, dish.stock, dish.selectedImage)
      .then (async () => {
        await nextTick();
        router.push('/dashboard')
      })
  } catch (err) {
    console.log(err.response?.data)
  }
}

</script>

<template>
  <div v-if='authStore.isAdmin' class="w-1/2">
    <h1 class="text-2xl font-bold text-center my-16">Yemek Ekle</h1>
    <form class="flex flex-col gap-10" @submit.prevent="addDish">
      <input v-model="dish.name" class="rounded-md p-3" placeholder="Yemek Adı" type="text">
      <input v-model="dish.description" class="rounded-md p-3" placeholder="Açıklama" type="text">
      <input v-model="dish.price" class="rounded-md p-3" placeholder="Fiyat" type="number">
      <input v-model="dish.stock" class="rounded-md p-3" placeholder="Stok" type="number">
      <input type="file" @change="handleImageChange">

      <button class="w-28 m-auto bg-white border-solid border border-gray-400 rounded-md" type="submit">Yemek Ekle
      </button>
    </form>
  </div>
  <div v-else class="w-1/2">
    <p>Bu sayfaya erişim yetkiniz yok.</p>
  </div>
</template>
