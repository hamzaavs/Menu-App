import { createWebHistory , createRouter } from 'vue-router'

import Dishes from "@/views/Dishes.vue";
import DishDetail from "@/views/DishDetail.vue";
import Register from "@/views/Register.vue";
import Login from "@/views/Login.vue";
import Profile from "@/views/Profile.vue";
import {useAuthStore} from "@/store/auth.js";
import AddDish from "@/views/AddDish.vue";


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
    },
    {
        path: '/profile',
        component: Profile,
        meta: { requiresAuth: true },
        name: 'profile'
    },
    {
        path: '/add-dish',
        component: AddDish,
        meta: { requiresAuth: true },
        name: 'add-dish'
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach(async (to, from, next) => {
    const authStore = useAuthStore();

    if (!authStore.isAuthenticated) {
        await authStore.fetchUser();
    }

    if (to.meta.requiresAuth && !authStore.isAuthenticated) {
        next("/");
    } else {
        next();
    }
});


export default router;
