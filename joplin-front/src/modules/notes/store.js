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
      is_todo: 0
    },
    notes: []
  },

  mutations,
  actions,
  getters
}

export default store
