<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";

const products = ref([{
  name: "",
  description: "",
  price: "",
  stock: ""
}])

const listProducts = async () =>{
  await axios.get("http://127.0.0.1:8000/dishes/list/")
    .then((res) => {
      products.value = res.data;
    })
}

onMounted(() => {
  listProducts();
})

</script>


<template>
  <body class="w-screen h-screen bg-primary flex justify-center items-center">
    <div class="w-10/12 grid grid-cols-3 gap-10 mt-28">
      <div
        v-for="item in products"
        :key="item.name"
        class="text-center bg-white p-10 shadow-lg rounded-md"
      >
        <h1 class="text-title text-2xl font-bold mb-2">{{ item.name }}</h1>
        <p class="text-description text-lg mb-4">{{ item.description }}</p>
        <p class="text-price text-right text-base">{{ item.price }}₺</p>
        <div>
          <p
            v-if="item.stock> 10"
            class="text-green-500 text-right text-base">
            {{ item.stock }} Adet kaldı
          </p>
          <p
            v-else-if="item.stock > 0 && item.stock < 10"
            class="text-yellow-500 text-right text-base">
            {{ item.stock }} Adet kaldı
          </p>
          <p
            v-else
            class="text-red-500 text-right text-base">
            Stokta yok
          </p>
        </div>
      </div>
    </div>
  </body>
</template>

