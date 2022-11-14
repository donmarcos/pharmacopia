import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import { Hub } from "@aws-amplify/core"
import Auth from "@aws-amplify/auth"
import Login from '../components/Login.vue'
import store from '../store/index.js'


let user;

getUser().then((user) => {
    if (user) {
        router.push({path: '/'});
    }
});

function getUser() {
    return Auth.currentAuthenticatedUser().then((data) => {
        if (data && data.signInUserSession) {
            store.commit('setUser', data);
            return data;
        }
    }).catch(() => {
        store.commit('setUser', null);
        return null;
    });
}

Hub.listen("auth", async (data) => {
    if (data.payload.event === 'signOut'){
        user = null;
        store.commit('setUser', null);
        router.push({path: '/login'});
    } else if (data.payload.event === 'signIn') {
        user = await getUser();
        router.push({path: '/'});
    }
});

const routes = [
  {
  path: '/',
  name: 'Home',
        component: Home,
  meta: { requiresAuth: true}
 },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
  path: '/home',
  name: 'home',
      component: Home
},
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
    meta: { requiresAuth: true}
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeResolve(async (to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        user = await getUser();
        if (!user) {
            return next({
                path: '/login'
            });
        }
        return next()
    }
    return next()
});

export default router

