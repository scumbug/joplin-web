import tagsApi from './api'
import types from './types'

export const actions = {
  [types.TAG_FETCH_ALL]: async ({ commit }) => {
    commit(types.TAG_SET_ALL, await tagsApi.fetchTags())
  },

  [types.TAG_FETCH]: async ({ commit }, tag) => {
    commit(types.TAG_SET, tag)
  },

  [types.TAG_CREATE]: async ({ commit }, tag) => {
    commit(types.TAG_APPEND, await tagsApi.createTag(tag))
  },

  [types.TAG_DELETE]: async ({ commit }, id) => {
    await tagsApi.deleteTag(id)
    commit(types.TAG_REMOVE, id)
  }
}

export default actions
