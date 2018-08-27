import foldersApi from './api'
import types from './types'

export const actions = {
  [types.FOLDER_FETCH_ALL]: async ({ commit }) => {
    commit(types.FOLDER_SET_ALL, await foldersApi.fetchFolders())
  },

  [types.FOLDER_CREATE]: async ({ commit }, folder) => {
    commit(types.FOLDER_APPEND, await foldersApi.createFolder(folder))
  },

  [types.FOLDER_DELETE]: async ({ commit }, id) => {
    await foldersApi.deleteFolder(id)
    commit(types.FOLDER_REMOVE, id)
  }
}

export default actions
