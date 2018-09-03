export const getters = {

  getFolders: (state) => state.folders,

  getFolderById: (state, getters) => (id) => getters.getFolders.filter(folder => folder.id === id)
}

export default getters
