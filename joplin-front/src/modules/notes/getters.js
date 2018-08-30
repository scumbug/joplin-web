export const getters = {

  getNote: (state) => state.note,
  getNotes: (state) => state.notes,

  getFolders2 (state, getters, rootState, rootGetters) {
    return rootGetters['folders/getFolders']
  },

  getNotesCount: (state, getters) => getters.getNotes.length
}

export default getters
