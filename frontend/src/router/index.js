import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

// 解决在当前页面再次点击 router-link 出现的报错
const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}

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
    },
    {
      path: '/addAdvertisement',
      component: () => import('../components/addAdvertisement')
    }
  ]
})

