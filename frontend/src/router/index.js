import { createWebHistory , createRouter } from 'vue-router'

import Dishes from "@/views/Dishes.vue";
import DishDetail from "@/views/DishDetail.vue";
import Register from "@/views/Register.vue";
import Login from "@/views/Login.vue";


const routes = [
    {
        path: '/',
        component: Dishes,
        name: 'home'
    },
    {
        path: `/dish/:id`,
        component: DishDetail,
        name: 'dish',
    },
    {
        path: '/register',
        component: Register,
        name: 'register'
    },
    {
        path: '/login',
        component: Login,
        name: 'login'
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router;
