<script setup>
import Navbar from "@/component/Navbar.vue";
</script>

<template>
  <div class="w-screen h-screen bg-gray-100 flex justify-center items-center font-sans">
    <Navbar />
    <slot></slot>
  </div>
</template>

<style scoped>

</style>
