import Notes from './components/Notes.vue'

export const routes = [
  { path: '/notes', name: 'allNotes', component: Notes, props: true },
  { path: '/notes/:id', name: 'myNote', component: Notes, props: true }
]

export default routes
