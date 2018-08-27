export const getters = {

  getNotes: (state) => state.notes,

  getFolders2 (state, getters, rootState, rootGetters) {
    return rootGetters['folders/getFolders']
  },

  getNoteById: (state, getters) => (id) => getters.getNotes.find(note => note.id === id),
  getNotesByTag: (state, getters) => (tag) => getters.getNotes.find(note => note.tag === tag),
  getNotesByFolder: (state, getters) => (folder) => getters.getNotes.find(note => note.folder === folder),

  getNotesByFolderCount: (state, getters) => getters.getNotesByFolder.length
  // getNotesCount: (state, getters) => getters.getNotes.length
}

export default getters
