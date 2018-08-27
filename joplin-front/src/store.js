import Vue from 'vue'
import Vuex from 'vuex'

import folders from './modules/folders'
import notes from './modules/notes'
import tags from './modules/tags'

Vue.use(Vuex)

export const store = new Vuex.Store({
  strict: true,

  modules: {
    folders: folders.store,
    notes: notes.store,
    tags: tags.store
  }
})

export default store
