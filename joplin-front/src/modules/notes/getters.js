// helper to map form fields to getters/setters
import { createHelpers } from 'vuex-map-fields'

const { getNoteField } = createHelpers({
  getterType: 'getNoteField'
})

export const getters = {

  getNote: (state) => state.note,
  getNotes: (state) => state.notes,

  getFolders2 (state, getters, rootState, rootGetters) {
    return rootGetters['folders/getFolders']
  },
  getNoteField
}

export default getters
