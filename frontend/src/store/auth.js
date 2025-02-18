import { defineStore } from "pinia";
import api from "@/api/axios";

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    isAuthenticated: false,
    token: localStorage.getItem("token") || null
  }),

  actions: {
    async register(name, surname, email, phone, password) {
      try {
        await api.post("/user/register/", {
          name,
          surname,
          email,
          phone,
          password,
        });
        return true
      } catch (err) {
        console.log(err.response?.data)
      }
    },

    async login(email, password) {
      try {
        const response = await api.post("/user/login/", {
          email,
          password,
        });

        const token = response.data.access_token;
        localStorage.setItem("token", token);
        api.defaults.headers.common["Authorization"] = `Bearer ${token}`;

        this.isAuthenticated = true
        await this.fetchUser()
      } catch (err) {
        console.log(err.response?.data)
      }
    },

    async fetchUser() {
      try {
        const token = localStorage.getItem("token");
        if (!token) return;

        api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
        const response = await api.get("/user/profile/");
        this.user = response.data;
        this.isAuthenticated = true;
      } catch (err) {
        console.log(err.response?.data);
        this.isAuthenticated = false; // Eğer hata varsa giriş yapılmadı olarak işaretle
      }
    },

    async logout() {
      try {
        await api.post("/user/logout/");
        this.user = null;
        this.isAuthenticated = false;
        localStorage.removeItem("token");
      } catch (err) {
        console.log(err.response?.data)
      }
    }
  }
})

