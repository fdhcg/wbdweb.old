import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Data from '@/components/Data'
import Docs from '@/components/Docs'
import Research from '@/components/Research'
import Zeppelin from '@/components/Zeppelin'
import About from '@/components/About'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/data',
      name: 'Data',
      component: Data
    },
    {
      path: '/docs',
      name: 'Docs',
      component: Docs
    },
    {
      path: '/research',
      name: 'Research',
      component: Research
    },
    {
      path: '/zeppelin',
      name: 'Zeppelin',
      component: Zeppelin
    },
    {
      path: '/about',
      name: 'About',
      component: About
    }
  ]
})
