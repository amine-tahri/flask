import { createRouter, createWebHistory } from 'vue-router';
import UserList from '../views/user-list.vue';
import LoginPage from '../views/login.vue';
import store from '../store'; // ✅ Import store

const routes = [
  {
    path: '/',
    redirect: '/login', // Default route redirects to login
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage,
  },
  {
    path: '/users',
    name: 'users',
    component: UserList,
    meta: {
      requiresAuth: true, // ✅ Protect this route
    },
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

// ✅ Navigation guard to protect routes
router.beforeEach((to, from, next) => {
  const isLoggedIn = store.getters.isLoggedIn;

  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!isLoggedIn) {
      return next('/login');
    }
  }

  // If already logged in and trying to access login page
  if (to.path === '/login' && isLoggedIn) {
    return next('/users');
  }

  next();
});

export default router;
