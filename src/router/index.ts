import { createRouter, createWebHistory } from 'vue-router';
import { ROUTE_NAMES } from '@/constants/routeNames';
import { useTokens } from '@/composables/useTokens';
import AuthorizationLayout from '@/layouts/AuthorizationLayout.vue';
import DefaultLayout from '@/layouts/DefaultLayout.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/login',
      component: AuthorizationLayout,
      children: [
        {
          path: '',
          name: ROUTE_NAMES.LoginPage,
          component: async () => import('@/pages/LoginPage.vue'),
          meta: {
            isPublic: true,
          },
        },
      ],
    },
    {
      path: '/',
      component: DefaultLayout,
      children: [
        {
          path: '',
          name: ROUTE_NAMES.HomePage,
          component: async () => import('@/pages/HomePage.vue'),
        },
      ],
    },
  ],
});

router.beforeEach((to, from, next) => {
  const { getRefresh, getAccess } = useTokens(localStorage);

  if (!to.matched.some((record) => record.meta?.isPublic)) {
    const access = getAccess();
    const refresh = getRefresh();

    if (!access && !refresh) {
      return next({ name: ROUTE_NAMES.LoginPage });
    }
  }

  next();
});

export default router;
