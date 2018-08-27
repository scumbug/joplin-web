import Vue from 'vue'
import Router from 'vue-router'

import folders from './modules/folders'
import notes from './modules/notes'
import tags from './modules/tags'

Vue.use(Router)

export const router = new Router({
  mode: 'history',
  routes: [
    ...folders.routes,
    ...notes.routes,
    ...tags.routes
  ]
})

export default router
