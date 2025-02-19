<script setup>
import {useAuthStore} from "@/store/auth.js";

const authStore = useAuthStore();

const logout = async () => {
  await authStore.logout();
}

</script>

<template>
  <nav class="bg-gradient-to-r from-orange-50 to-pink-100 text-white shadow-lg p-5 flex justify-between fixed top-0 w-screen ">
    <router-link to="/" class="text-black font-bold text-2xl">Yemeğim</router-link>
    <div class="flex space-x-4" v-if="!authStore.isAuthenticated">
      <router-link to="/login" class="border border-black rounded px-4 py-2 text-black hover:bg-white hover:text-orange-500 hover:border-white transition">Giriş Yap</router-link>
      <router-link to="/register" class="bg-white text-orange-500 border border-white rounded px-4 py-2 hover:bg-orange-600 hover:text-white transition">Kayıt Ol</router-link>
    </div>
    <div v-else class="flex space-x-4">
      <router-link to="/profile" class="capitalize border border-black rounded px-4 py-2 text-black hover:bg-white hover:text-orange-500 hover:border-white transition">
        {{ authStore.user?.name }}</router-link>
      <button @click="logout" class="bg-white text-orange-500 border border-white rounded px-4 py-2 hover:bg-orange-600 hover:text-white transition">Çıkış Yap</button>
    </div>
  </nav>
</template>

<style scoped>

</style>
