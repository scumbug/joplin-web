import types from './types'

export const mutations = {
  [types.FOLDER_SET_ALL]: (state, folders) => {
    state.folders = folders
  },

  [types.FOLDER_SET]: (state, folder) => {
    state.folder = folder
  },

  [types.FOLDER_APPEND]: (state, folder) => {
    state.folder.push(folder)
  },

  [types.FOLDER_CHANGE]: (state, folder) => {
    const el = state.folders.find(t => t.id === folder.id)
    state.folders.splice(state.folders.indexOf(el), 1, folder)
  },

  [types.FOLDER_REMOVE]: (state, id) => {
    const el = state.folder.find(folder => folder.id === id)
    state.folder.splice(state.folder.indexOf(el), 1)
  }
}

export default mutations
