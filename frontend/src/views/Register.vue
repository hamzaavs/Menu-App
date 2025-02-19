<script setup>
import { ref } from 'vue'
import {useAuthStore} from "@/store/auth.js";
import {useRouter} from "vue-router";

const email = ref('')
const password = ref('')
const name = ref('')
const surname = ref('')
const phone = ref()
const message = ref('')

const authStore = useAuthStore();
const router = useRouter();



const register = async () => {
  const success = await authStore.register(name.value, surname.value, email.value , phone.value, password.value);
  if (success) {
    router.push('/login');
  }
}

</script>

<template>
  <div class="w-1/2">
    <h1 class="text-2xl font-bold text-center my-16">Kayıt Ol</h1>
    <form @submit.prevent="register" class="flex flex-col gap-10">
      <input v-model="name" type="text" placeholder="İsim">
      <input v-model="surname" type="text" placeholder="Soyisim">
      <input v-model="email" type="email" placeholder="Email">
      <input v-model="phone" type="tel" placeholder="Telefon Numarası">
      <input v-model="password" type="password" placeholder="Şifre">

      <button type="submit" class="w-28 m-auto bg-white border-solid border border-gray-400 rounded-md">Kayıt Ol
      </button>
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
