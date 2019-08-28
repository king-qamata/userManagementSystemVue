import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

export default new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/home',
      component: () => import('../views/Customers')
    },
    {
      path: '/about',
      component: () => import('../views/About')
    },
    {
      path: '/add',
      component: () => import('../views/Add')
    },
    {
      path: '/login',
      component: () => import('../views/Login')
    }
  ]
})

