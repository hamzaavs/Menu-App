<script setup>
import {onMounted} from 'vue'
import {useDishStore} from "@/store/dish.js";
import {useAuthStore} from "@/store/auth.js";

const dishStore = useDishStore()
const authStore = useAuthStore()


onMounted(() => {
  dishStore.list()
})
</script>

<template>
  <div v-if="authStore.isAdmin" class="w-1/2">
    <h1 class="text-2xl font-bold text-center my-16">Yemekler</h1>
    <div class="relative overflow-x-auto shadow-md sm:rounded-lg mt-20">
      <table class="w-full text-sm text-left rtl:text-right text-gray-500 ">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 border border-solid border-gray-200 ">
        <tr>
          <th class="px-6 py-3">
            Yemek Adı
          </th>
          <th class="px-6 py-3">
            Fiyat (TL)
          </th>
          <th class="px-6 py-3">
            Stok
          </th>
          <th class="px-6 py-3">
            İşlemler
          </th>
          <th class="px-6 py-3 text-right">
            <router-link
              class="inline-flex items-center px-4 py-2 bg-green-600 text-white font-medium rounded-md hover:bg-green-700 transition-colors"
              to="/add-dish"
            >
              Yemek Ekle
            </router-link>
          </th>

        </tr>
        </thead>
        <tbody>
        <tr
          v-for="items in dishStore.dishes"
          class="odd:bg-white even:bg-gray-50 border-b">
          <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap" scope="row">
            {{ items.name }}
          </th>
          <td class="px-6 py-4">
            {{ items.price }}₺
          </td>
          <td class="px-6 py-4">
            {{ items.stock }} Adet Kaldı
          </td>
          <td class="px-6 py-4 flex flex-row gap-6">
            <router-link :to="`/edit-dish/${items.unique_id}`" class="font-medium text-blue-600 hover:underline">Düzenle
            </router-link>
            <button class="font-medium text-red-600 hover:underline" @click="dishStore.delete(items.unique_id)">Sil</button>
          </td>
          <td></td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
  <div v-else>
    <p>Bu sayfaya erişim yetkiniz yok.</p>
  </div>
</template>
