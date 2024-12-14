import { createWebHistory , createRouter } from 'vue-router'

import Dishes from "@/views/Dishes.vue";
import DishDetail from "@/views/DishDetail.vue";

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
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router;
