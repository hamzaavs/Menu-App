<script setup>
import {nextTick, onMounted, reactive} from 'vue'
import { useRoute } from 'vue-router'
import {useAuthStore} from "@/store/auth.js";
import {useDishStore} from "@/store/dish.js";
import router from "@/router/index.js";

const dishStore = useDishStore()
const authStore = useAuthStore()
const route = useRoute()
const id = route.params.id

const dishInfo = reactive({
  name: '',
  description: '',
  price: 0.0,
  stock: 0
})

onMounted(() => {
  dishStore.detail(id)
})

const updateDish = async () => {
  try {
    await dishStore.update(id, dishInfo.name, dishInfo.description, dishInfo.price, dishInfo.stock)
      .then(async () => {
        await nextTick();
        await router.push('/dashboard')
      })
  } catch (err) {
    console.log(err.response?.data)
  }
}

</script>

<template>
  <div v-if='authStore.isAdmin' class="w-1/2">
    <h1 class="text-2xl font-bold text-center my-16">Yemek Düzenle</h1>
    <h2 class="text-xl font-semibold text-center my-16">  Yemek Adı: {{ dishStore.dish?.name }}
    </h2>
    <form class="flex flex-col gap-10" @submit.prevent="updateDish">
      <input v-model="dishInfo.name" class="rounded-md p-3" placeholder="Yemek Adı" type="text">
      <input v-model="dishInfo.description" class="rounded-md p-3" placeholder="Açıklama" type="text">
      <input v-model="dishInfo.price" class="rounded-md p-3" placeholder="Fiyat" type="number">
      <input v-model="dishInfo.stock" class="rounded-md p-3" placeholder="Stok" type="number">
      <button class="w-28 m-auto bg-white border-solid border border-gray-400 rounded-md" type="submit">Yemek Düzenle
      </button>
    </form>
  </div>
  <div v-else class="w-1/2">
    <p>Bu sayfaya erişim yetkiniz yok.</p>
  </div>
</template>

<style scoped>

</style>
