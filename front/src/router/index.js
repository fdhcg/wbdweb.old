import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home'
import Data from '@/views/Data'
import Docs from '@/views/Docs'
import Research from '@/views/Research'
import Zeppelin from '@/views/Zeppelin'
import About from '@/views/About'

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
