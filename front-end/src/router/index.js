import { createRouter, createWebHistory } from 'vue-router'
import ThingsView from '../views/ThingsView.vue'

const routes = [
    {
        path: "/",
        name: "Home",
        component: ThingsView
    },
];

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
});

export default router;