import getters from './getters'
import actions from './actions'
import mutations from './mutations'

export const store = {
  namespaced: true,

  state: {
    folder: {
      id: '',
      title: '',
      parent_id: '',
      children: []
    },
    folders: []
  },

  mutations,
  actions,
  getters
}

export default store
