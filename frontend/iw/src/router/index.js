import Vue from 'vue'
import Router from 'vue-router'

const Home = () => import('@/components/Home')
const Daily = () => import('@/components/Daily')
const About = () => import('@/components/About')
const Market = () => import('@/components/Market')
const KLine = () => import ('@/components/KLine')

Vue.use(Router)

const originalPush = Router.prototype.push
Router.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}

export default new Router({
  routes: [
    {
      path: '',
      redirect: '/home'
    },
    {
      path: '/home',
      component: Home,
      children: [
        {
          path: 'daily',
          component: Daily
        }
      ]
    },
    {
      path: '/about',
      component: About
    },
    {
      path: '/market/:code',
      component: Market
    },
    {
      path: '/kline',
      component: KLine
    }
  ],
  mode: 'history'
})
