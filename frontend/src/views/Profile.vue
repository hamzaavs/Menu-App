<script setup>

import { useRouter } from "vue-router";
import {useAuthStore} from "@/store/auth.js";
import {onMounted} from "vue";

const authStore = useAuthStore();
const router = useRouter();

onMounted(async () => {
  await authStore.fetchUser();
});
const handleLogout = async () => {
  await authStore.logout();
  router.push("/login");
};
</script>

<template>
  <div v-if="authStore.isAuthenticated">
    <h2>Merhaba, {{ authStore.user?.surname }}</h2>
    <p>Email: {{ authStore.user?.email }}</p>
    <p>Telefon: {{ authStore.user?.phone }}</p>
    <button @click="handleLogout">Çıkış Yap</button>
  </div>
  <div v-else>
    <p>Lütfen giriş yapınız.</p>
  </div>
</template>
