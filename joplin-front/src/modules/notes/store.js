import getters from './getters'
import actions from './actions'
import mutations from './mutations'

export const store = {
  namespaced: true,

  state: {
    note: {
      id: 0,
      title: '',
      body: '',
      parent: {
        id: 0,
        parent_id: 0
      },
      is_todo: 0,
      todo_due: 0,
      todo_completed: 0,
      created_time: 0,
      updated_time: 0,
      source_url: '',
      author: '',
      latitude: 0,
      longitude: 0,
      altitude: 0,
      source: '',
      source_application: ''
    },
    notes: []
  },

  mutations,
  actions,
  getters
}

export default store
