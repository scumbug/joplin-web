export const getters = {

  getNote: (state) => state.note,
  getNotes: (state) => state.notes,

  getFolders2 (state, getters, rootState, rootGetters) {
    return rootGetters['folders/getFolders']
  },

  getNoteById: (state, getters) => (id) => getters.getNotes.find(note => note.id === id),
  getNotesByTag: (state, getters) => (tag) => getters.getNotes.find(note => note.tag === tag),
  getNotesByFolder: (state, getters) => (folder) => getters.getNotes.find(note => note.folder === folder),

  getNotesByTagCount: (state, getters) => (id) => getters.getNotesByTag(id).length,
  getNotesByFolderCount: (state, getters) => (folder) => getters.getNotesByFolder(folder).length,
  // getNotesByFolderCount: (state, getters) => (folder) => state.notes.find(note => note.folder === folder).length,
  getNotesCount: (state, getters) => getters.getNotes.length
}

export default getters
