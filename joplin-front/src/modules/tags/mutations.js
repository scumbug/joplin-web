import types from './types'

export const mutations = {
  [types.TAG_SET_ALL]: (state, tags) => {
    state.tags = tags
  },

  [types.TAG_SET]: (state, tag) => {
    state.tag = tag
  },

  [types.TAG_APPEND]: (state, tag) => {
    state.tag.push(tag)
  },

  [types.TAG_CHANGE]: (state, tag) => {
    const el = state.tags.find(t => t.id === tag.id)
    state.tags.splice(state.tags.indexOf(el), 1, tag)
  },

  [types.TAG_REMOVE]: (state, id) => {
    const el = state.tags.find(tag => tag.id === id)
    state.tags.splice(state.tags.indexOf(el), 1)
  }
}

export default mutations
