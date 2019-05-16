export const getters = {

  getFolders: (state) => state.folders,
  getFolderById: (state, getters) => (parentId) => getters.getFolders.filter(folder => folder.parent_id === parentId)
}

export default getters
