import getters from './getters'
import actions from './actions'
import mutations from './mutations'

export const store = {
  namespaced: true,

  state: {
    tags: []
  },

  mutations,
  actions,
  getters
}

export default store
