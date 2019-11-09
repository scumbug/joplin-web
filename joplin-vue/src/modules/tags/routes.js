import Tags from './components/Tags.vue'

export const routes = [
  { path: '/tags', name: 'allTags', component: Tags, props: true },
  { path: '/tags/:id', name: 'myTag', component: Tags, props: true }

]

export default routes
