<script setup>

import {useRouter} from "vue-router";
import {useAuthStore} from "@/store/auth.js";
import {onMounted} from "vue";

const authStore = useAuthStore();
const router = useRouter();

onMounted(async () => {
  await authStore.fetchUser();
});

</script>

<template>
  <div v-if="authStore.isAuthenticated" class="bg-white w-4/5 rounded mt-16">
    <div class="my-16">
      <p class="text-3xl font-bold text-center capitalize mb-2">Merhaba, {{ authStore.user?.name }}
        {{ authStore.user?.surname }}</p>
      <p class="text-center text-sm font-medium">Email: {{ authStore.user?.email }}</p>
    </div>
    <div>
      <div class="bg-gray-100 mx-10 my-5 p-5 rounded-2xl">
        <p class="text-xs">Ad</p>
        <p class="text-lg font-bold capitalize">{{ authStore.user?.name }}</p>
      </div>
      <div class="bg-gray-100 mx-10 my-5 p-5 rounded-2xl">
        <p class="text-xs">Soyad</p>
        <p class="text-lg font-bold capitalize">{{ authStore.user?.surname }}</p>
      </div>
      <div class="bg-gray-100 mx-10 my-5 p-5 rounded-2xl">
        <p class="text-xs">E-posta</p>
        <p class="text-lg font-bold">{{ authStore.user?.email }}</p>
      </div>
      <div class="bg-gray-100 mx-10 my-5 p-5 rounded-2xl">
        <p class="text-xs">Telefon Numarası </p>
        <p class="text-lg font-bold">{{ authStore.user?.phone }}</p>
      </div>


    </div>

  </div>
  <div v-else>
    <p>Lütfen giriş yapınız.</p>
  </div>
</template>
