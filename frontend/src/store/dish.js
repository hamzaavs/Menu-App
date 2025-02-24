import {defineStore} from "pinia";
import api from "@/api/axios";

export const useDishStore = defineStore('dish', {
  state: () => ({
    dishes: [],
    dish: null,
  }),

  actions: {
    async list() {
      try {
        const response = await api.get('/dishes/list/')
        this.dishes = response.data
      } catch (err) {
        console.log(err)
      }
    },

    async create(name, description, price, stock) {
      try {
        return await api.post('/dishes/', {
          name,
          description,
          price,
          stock
        })
      } catch (err) {
        console.log(err)
      }
    },

    async detail(id) {
      try {
      const response = await api.get(`/dishes/${id}/`)
        this.dish = response.data
        console.log(this.dish)
      } catch (err) {
        console.log(err)
      }
    }
  }
})
