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
        console.log(err.response?.data)
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
        console.log(err.response?.data)
      }
    },

    async detail(id) {
      try {
      const response = await api.get(`/dishes/${id}/`)
        this.dish = response.data
        console.log(this.dish)
      } catch (err) {
        console.log(err.response?.data)
      }
    },

    async update(id, name, description, price, stock) {
      try {
        await api.put(`dishes/${id}/`, {
          name,
          description,
          price,
          stock
        })
      } catch (err) {
        console.log(err.response?.data)
      }
    },

    async delete(id) {
      try {
        await api.delete(`/dishes/${id}/`)
      } catch (err) {
        console.log(err.response?.data)
      }
    }
  }
})
