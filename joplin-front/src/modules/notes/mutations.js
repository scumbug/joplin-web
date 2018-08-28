import types from './types'

export const mutations = {
  [types.NOTE_SET_ALL]: (state, notes) => {
    state.notes = notes
  },

  [types.NOTE_SET]: (state, note) => {
    state.note = note
  },

  [types.NOTE_APPEND]: (state, note) => {
    state.note.push(note)
  },

  [types.NOTE_CHANGE]: (state, note) => {
    const el = state.notes.find(t => t.id === note.id)
    state.notes.splice(state.notes.indexOf(el), 1, note)
  },

  [types.NOTE_REMOVE]: (state, id) => {
    const el = state.note.find(note => note.id === id)
    state.note.splice(state.note.indexOf(el), 1)
  }
}

export default mutations
