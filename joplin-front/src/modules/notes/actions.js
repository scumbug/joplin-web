import notesApi from './api'
import types from './types'

export const actions = {
  [types.NOTE_FETCH_ALL]: async ({ commit }) => {
    commit(types.NOTE_SET_ALL, await notesApi.fetchNotes())
  },

  [types.NOTE_CREATE]: async ({ commit }, note) => {
    commit(types.NOTE_APPEND, await notesApi.createNote(note))
  },

  [types.NOTE_DELETE]: async ({ commit }, id) => {
    await notesApi.deleteNote(id)
    commit(types.NOTE_REMOVE, id)
  }
}

export default actions
