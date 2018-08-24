import Vue from 'vue'
import Router from 'vue-router'
import Notes from './components/Notes.vue'
Vue.use(Router)

export default new Router({
  routes: [
    { path: '/notes/folder/:bookName', component: Notes, name: 'notesbybook', props: true },
    { path: '/notes/tag/:tagName', component: Notes, name: 'notesbytag', props: true }
  ]
})
