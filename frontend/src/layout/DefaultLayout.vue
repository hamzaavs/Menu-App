<script setup>
import Navbar from "@/component/Navbar.vue";
</script>

<template>
  <div class="flex flex-col max-w-screen h-screen bg-gray-100 justify-between">
    <div>
      <Navbar/>
      <div class="bg-gray-100 flex flex-col justify-center items-center mt-16 pb-10">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
