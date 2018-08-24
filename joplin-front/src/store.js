import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(Vuex)

Vue.use(VueAxios, axios)

export default new Vuex.Store({
  state: {
    notes: [],
    note: {},
    books: [],
    notebook: {},
    title: '',
    url: '',
    tags: [],
    tag: {}
  },
  getters: {
    notes: state => {
      return state.notes
    },
    note: state => {
      return state.note
    },
    books: state => {
      return state.books
    },
    book: state => {
      return state.book
    },
    tags: state => {
      return state.tags
    },
    tag: state => {
      return state.tag
    }
  },
  actions: {
    /* Folders */
    loadBooks: async ({ commit }) => {
    //  return new Promise((resolve, reject) => {
      await axios.get('http://127.0.0.1:8001/api/jw/folders/').then((res) => {
        if (res.data.count > 0) {
          commit('mLoadBooks', res.data.results)
          console.log(res.data.results)
          // resolve()
        }
      })
    // })
    },
    addBook: async ({ commit }, book) => {
      // add a note
      // default status to true
      await axios.post('http://127.0.0.1:8000/api/jw/folders/', book).then((res) => {
        // get the created ID and add it to the current note line
        book.id = res.data.id
        commit('mAddBook', book)
      }).catch((error) => {
        console.log(error)
      })
    },
    updateBook: ({ commit }, book) => {
      // update a Book
      axios.patch('http://127.0.0.1:8000/api/jw/folders/' + book.id + '/', book).then((res) => {
        commit('mUpdateBook', book)
      })
    },
    editBook: ({ commit }, book) => {
      // edit a book
      commit('mEditBook', { book })
    },
    removeBook: ({ commit }, id) => {
      // remove one folders
      axios.delete('http://127.0.0.1:8000/api/jw/folders/' + id + '/').then((res) => {
        commit('mRemoveNook', id)
      })
    },
    /* Notes */
    loadNotes: async ({ commit }) => {
    //  return new Promise((resolve, reject) => {
      await axios.get('http://127.0.0.1:8001/api/jw/notes/').then((res) => {
        if (res.data.count > 0) {
          commit('mLoadNotes', res.data.results)
          // resolve()
        }
      })
    // })
    },
    addNote: async ({ commit }, note) => {
      // add a note
      // default status to true
      await axios.post('http://127.0.0.1:8000/api/jw/notes/', note).then((res) => {
        // get the created ID and add it to the current note line
        note.id = res.data.id
        commit('mAddNote', note)
      }).catch((error) => {
        console.log(error)
      })
    },
    updateNote: ({ commit }, note) => {
      // update a note
      axios.patch('http://127.0.0.1:8000/api/jw/notes/' + note.id + '/', note).then((res) => {
        commit('mUpdateNote', note)
      })
    },
    editNote: ({ commit }, note) => {
      // edit a note
      commit('mEditNote', { note })
    },
    removeNote: ({ commit }, id) => {
      // remove one note
      axios.delete('http://127.0.0.1:8000/api/jw/notes/' + id + '/').then((res) => {
        commit('mRemoveNote', id)
      })
    },
    /* Tags */
    loadTags: async ({ commit }) => {
    //  return new Promise((resolve, reject) => {
      await axios.get('http://127.0.0.1:8001/api/jw/tags/').then((res) => {
        if (res.data.count > 0) {
          commit('mLoadTags', res.data.results)
          // resolve()
        }
      })
    // })
    },
    notesByBook: async ({ commit }, book) => {
      await axios.get('http://127.0.0.1:8001/api/jw/notes/folder/' + book).then((res) => {
        if (res.data.count > 0) {
          commit('mLoadNotes', res.data.results)
        }
      })
    },
    notesByTag: async ({ commit }, tag) => {
      await axios.get('http://127.0.0.1:8001/api/jw/notes/tag/' + tag).then((res) => {
        if (res.data.count > 0) {
          commit('mLoadNotes', res.data.results)
        }
      })
    },
    addTag: async ({ commit }, tag) => {
      // add a tag
      // default status to true
      await axios.post('http://127.0.0.1:8000/api/jw/tags/', tag).then((res) => {
        // get the created ID and add it to the current note line
        tag.id = res.data.id
        commit('mAddTag', tag)
      }).catch((error) => {
        console.log(error)
      })
    },
    updateTag: ({ commit }, tag) => {
      // update a tag
      axios.patch('http://127.0.0.1:8000/api/jw/tags/' + tag.id + '/', tag).then((res) => {
        commit('mUpdateTag', tag)
      })
    },
    editTag: ({ commit }, tag) => {
      // edit a tag
      commit('mEditTag', { tag })
    },
    removeTag: ({ commit }, id) => {
      // remove one tag
      axios.delete('http://127.0.0.1:8000/api/jw/tag/' + id).then((res) => {
        commit('mRemoveTag', id)
      })
    }
  },
  mutations: {
    /* Notes */
    mLoadNotes (state, notes) {
      state.notes = notes
    },
    mAddNote (state, payload) {
      state.notes.push(payload)
      state.note = {}
    },
    mEditNote (state, {note}) {
      state.note = note
    },
    mRemoveNote (state, id) {
      const el = state.notes.find(t => t.id === id)
      state.notes.splice(state.notes.indexOf(el), 1)
    },
    mUpdateNote (state, note) {
      const el = state.notes.find(t => t.id === note.id)
      state.notes.splice(state.notes.indexOf(el), 1, note)
      state.note = {}
    },
    /* Folders */
    mLoadBooks (state, books) {
      state.books = books
    },
    mAddBook (state, payload) {
      state.books.push(payload)
      state.book = {}
    },
    mEditBook (state, {book}) {
      state.book = book
    },
    mRemoveBook (state, id) {
      const el = state.books.find(t => t.id === id)
      state.books.splice(state.books.indexOf(el), 1)
    },
    mUpdateBook (state, book) {
      const el = state.books.find(t => t.id === book.id)
      state.books.splice(state.books.indexOf(el), 1, book)
      state.book = {}
    },
    /* Tags */
    mLoadTags (state, tags) {
      state.tags = tags
    },
    mAddTag (state, payload) {
      state.books.push(payload)
      state.tag = {}
    },
    mEditTag (state, {tag}) {
      state.tag = tag
    },
    mRemoveTag (state, id) {
      const el = state.tags.find(t => t.id === id)
      state.tags.splice(state.tags.indexOf(el), 1)
    },
    mUpdateTag (state, tag) {
      const el = state.tags.find(t => t.id === tag.id)
      state.tags.splice(state.tags.indexOf(el), 1, tag)
      state.tag = {}
    }
  }
})
