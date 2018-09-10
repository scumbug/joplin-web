<template>
  <div>
  <ul class="list-group">
    <book v-for="book in this.getFolders" :key="book.id">
      <a href="#" @click="notesByFolder(book)">{{ book.title }}</a>&nbsp;<span class="badge badge-secondary badge-pill">{{ book.nb_notes }}</span>
    </book>
  </ul>
  </div>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'

import Book from './Book'

import getters from '../getters'
import actions from '../actions'
import types from '../types'
import typesNote from '../../notes/types'
import typesTag from '../../tags/types'

const namespace = 'folders'
const { mapGetters, mapActions } = createNamespacedHelpers(namespace)

export default {
  data () {
    return {
      label: ''
    }
  },
  components: { Book },
  methods: {
    notesByFolder (folder) {
      let tag = {}
      this.$store.dispatch('folders/' + types.FOLDER_FETCH, folder)
      this.$store.dispatch('tags/' + typesTag.TAG_FETCH, tag)
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
