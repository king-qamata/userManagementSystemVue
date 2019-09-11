import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

// 解决在当前页面再次点击 router-link 出现的报错
const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: () => import('views/Root'),
      children: [
        {
          path: '/home',
          component: () => import('views/Home')
        },
        { path: '/customers',
          component: () => import('views/Customers')
        },
        {
          path: '/about',
          component: () => import('views/About')
        },
        {
          path: '/add',
          component: () => import('views/Add')
        },
        {
          path: '/addAdvertisement',
          component: () => import('@/components/addAdvertisement')
        }
      ]
    },
    {
      path: '/login',
      component: () => import('views/Login')
    }
  ]
})
router.beforeEach((to, from, next) => {
  // 当前会话下有效，关闭页面后清除
  const user = sessionStorage.getItem('user')
  if (to.path === '/login') {
    if (user) {
      next({ path: '/' })
    } else {
      next()
    }
  } else {
    if (user) {
      next()
    } else {
      next({ path: '/login' })
    }
  }
})

export default router
