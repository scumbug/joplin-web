import Folders from './components/Folders.vue'

export const routes = [
  { path: '/folders', name: 'allFolders', component: Folders, props: true },
  { path: '/folders/:id', name: 'myFolder', component: Folders, props: true }
]

export default routes
