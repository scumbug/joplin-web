<template>
    <div>
        <h3>Books</h3>
        <div class="panel-body">
            <input class="form-control" v-model="name" @keyup.enter="addBook()" type="text" placeholder="enter the book name">
            <span class="help is-danger" v-if="errors.has('name')" v-text="errors.getError('name')"></span>
        </div>
      <div class="articles">
        <ul class="list-group">
        <book v-for="book in this.getFolders" :key="book.id">
            <li class="list-group-item">
                <a href="#" @click="notesByBook(book.id)">{{ book.title }}</a>
            </li>
        </book>
        </ul>
      </div>
    </div>
</template>

<script>
/* errors class */
import Errors from '../../../core/Errors'
import Book from './Book'

import { createNamespacedHelpers } from 'vuex'

import getters from '../getters'
import actions from '../actions'
import types from '../types'

const namespace = 'folders'
const { mapGetters, mapActions } = createNamespacedHelpers(namespace)

export default {
  data () {
    return {
      name: '',
      page: 1,
      loading: true,
      errors: new Errors()
    }
  },
  components: {Book},
  methods: {
    /* create a book */
    addBook () {
      let payload = {
        name: this.name
      }
      this.$store.dispatch('folders/' + types.FOLDER_CREATE, payload)
    },
    getNotesByFolder (folder) {
      return this.$store.getters.getNotesByFolder(folder)
    },
    deleteFolder (id) {
      this.$store.dispatch('folders/' + types.FOLDER_DELETE, id)
    },
    ...mapActions(Object.keys(actions))
  },
  computed: {
    ...mapGetters(Object.keys(getters))
  },
  created () {
    this.$store.dispatch('folders/' + types.FOLDER_FETCH_ALL)
      .then(() => (this.loading = false))
  }
}
</script>
