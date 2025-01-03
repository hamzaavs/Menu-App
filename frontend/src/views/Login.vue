<script setup>
import { ref } from 'vue'
import axios from "axios";

const email = ref('')
const password = ref('')
const message = ref('')

const login = async () => {
  const response = await axios.post('http://127.0.0.1:8000/user/login/', {
    email: email.value,
    password: password.value
  })
  if (response.status === 200) {
    localStorage.setItem('token', response.data.token)
    localStorage.setItem('user', JSON.stringify(response.data.user))
    window.location.href = '/'
    message.value = 'Giriş yapıldı.'

  } else {
    alert('Giriş yapılamadı. Lütfen tekrar deneyiniz.')
  }
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
