import types from './types'
// helper to map form fields mutations
import { createHelpers } from 'vuex-map-fields'

const { updateNoteField } = createHelpers({
  mutationType: 'updateNoteField'
})

export const mutations = {
  [types.NOTE_NEW]: (state) => {
    state.note = {
      id: 0,
      title: '',
      body: '',
      parent: {
        id: 0,
        parent_id: 0
      },
      is_todo: 0
    },
    state.tag = ''
  },

  [types.NOTE_SET_ALL]: (state, notes) => {
    state.notes = notes
  },

  [types.NOTE_SET]: (state, note) => {
    state.note = note
  },

  [types.NOTETAG_SET]: (state, tag) => {
    state.tag = tag
  },

  [types.NOTE_APPEND]: (state, note) => {
    state.notes.push(note)
  },

  [types.NOTE_CHANGE]: (state, note) => {
    const el = state.notes.find(t => t.id === note.id)
    state.notes.splice(state.notes.indexOf(el), 1, note)
  },

  [types.NOTE_REMOVE]: (state, id) => {
    const el = state.notes.find(note => note.id === id)
    state.notes.splice(state.notes.indexOf(el), 1)
    state.note = {
      id: 0,
      title: '',
      body: '',
      parent: {
        id: 0,
        parent_id: 0
      },
      is_todo: 0
    }
  },
  updateNoteField
}

export default mutations
