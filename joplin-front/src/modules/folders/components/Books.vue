<template>
  <div>
<!--input class="form-control" v-model="name" @keyup.enter="addFolder()" type="text" placeholder="enter the book name">
  <span class="help is-danger" v-if="errors.has('name')" v-text="errors.getError('name')"></span-->
  <ul class="list-group">
    <book v-for="book in this.getFolders" :key="book.id">
      <a href="#" @click="notesByFolder(book.id)">{{ book.title }}</a>&nbsp;<span class="badge badge-primary badge-pill">{{ book.nb_notes }}<slot></slot></span>
    </book>
  </ul>
  </div>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'

/* errors class */
import Errors from '../../../core/Errors'
import Book from './Book'

import getters from '../getters'
import actions from '../actions'
import types from '../types'

import typesNote from '../../notes/types'

const namespace = 'folders'
const { mapGetters, mapActions } = createNamespacedHelpers(namespace)

export default {
  data () {
    return {
      name: '',
      errors: new Errors()
    }
  },
  components: { Book },
  methods: {
    /* create a folder */
    addFolder () {
      let payload = {
        name: this.name
      }
      this.$store.dispatch('folders/' + types.FOLDER_CREATE, payload)
    },
    deleteFolder (id) {
      this.$store.dispatch('folders/' + types.FOLDER_DELETE, id)
    },
    notesByFolder (folder) {
      this.$store.dispatch('notes/' + typesNote.NOTE_FETCH_FOLDER, folder)
    },
    ...mapActions(Object.keys(actions))
  },
  computed: {
    ...mapGetters(Object.keys(getters))
  },
  created () {
    this.$store.dispatch('folders/' + types.FOLDER_FETCH_ALL)
  }
}
</script>
