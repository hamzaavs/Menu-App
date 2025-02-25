<script setup>
import { ref } from 'vue'
import {useAuthStore} from "@/store/auth.js";
import {useRouter} from "vue-router";

const email = ref('')
const password = ref('')
const message = ref('')

const authStore = useAuthStore();
const router = useRouter();

const login = async () => {
  await authStore.login(email.value, password.value);
  router.push('/profile');
}

</script>

<template>
  <div class="w">
    <h1 class="text-2xl font-bold text-center my-16">Giriş Yap</h1>
    <form @submit.prevent="login" class="flex flex-col gap-10">
      <input v-model="email" type="email" placeholder="Email">
      <input v-model="password" type="password" placeholder="Şifre">
      <button class="w-28 m-auto bg-white border-solid border border-gray-400 rounded-md">Giriş Yap</button>
    </form>
    <p>{{ message }}</p>
  </div>
</template>

<style scoped>
input {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
</style>
