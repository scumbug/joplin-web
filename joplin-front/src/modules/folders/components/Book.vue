<template>
  <ul class="list-group">
    <li class="list-group-item justify-content-between align-items-center"
        v-if="book.parent_id == parent_book.id"
        v-for="book in this.getFolderById(parent_book.id)"
        :key="book.id">
        <a href="#" @click="notesByFolder(book)">{{ book.title }}</a>&nbsp;<span class="badge badge-secondary badge-pill">{{ book.nb_notes }}</span>
        <book :parent_book="book"/>
    </li>
  </ul>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'

import getters from '../getters'
import actions from '../actions'
import types from '../types'
import typesNote from '../../notes/types'
import typesTag from '../../tags/types'

const namespace = 'folders'
const { mapGetters, mapActions } = createNamespacedHelpers(namespace)

export default {
  name: 'Book',
  props: {
    parent_book: Object
  },
  computed: {
    ...mapGetters(Object.keys(getters))
  },
  methods: {
    notesByFolder (folder) {
      this.$store.dispatch('folders/' + types.FOLDER_FETCH, folder)
      this.$store.dispatch('tags/' + typesTag.TAG_FETCH, tag)
      this.$store.dispatch('notes/' + typesNote.NOTE_FETCH_FOLDER, folder)
    },
    ...mapActions(Object.keys(actions))
  }
}

</script>
