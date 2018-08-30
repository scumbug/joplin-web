export const getters = {

  getTags: (state) => state.tags,

  getTagById: (state, getters) => (id) => getters.getTags.filter(tag => tag.id === id),

  getTagsCount: (state, getters) => getters.getTags.length
}

export default getters
