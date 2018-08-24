<template>
    <div class="col-2">
      <h3>Books <button class="btn btn-success" @click="seen = !seen">Book</button></h3>
      <div class="panel-body" v-if="seen">
          <input class="form-control" v-model="name" @keyup.enter="addBook()" type="text" placeholder="enter the book name">
          <span class="help is-danger" v-if="errors.has('name')" v-text="errors.getError('name')"></span>
      </div>
      <div class="articles">
        <ul class="list-group">
        <book v-for="book in books" :key="book.id">
            <li class="list-group-item">
                <a href="#" @click="notesByBook(book.id)">{{ book.title }}</a>
            </li>
        </book>
        </ul>
      </div>
      <h3>Tags</h3>
        <div class="articles">
        <ul class="list-group">
        <tag v-for="tag in tags" :key="tag.id">
            <li class="list-group-item">
                <a href="#" @click="notesByTag(tag.id)">{{ tag.title }}</a>
            </li>
        </tag>
        </ul>
        </div>
    </div>
</template>

<script>
/* errors class */
import Errors from '../core/Errors'
import Tag from './Tag.vue'
import Book from './Book.vue'

import { mapActions } from 'vuex'

export default {
  data () {
    return {
      name: '',
      seen: false,
      // books: [],
      page: 1,
      errors: new Errors()
    }
  },
  components: {Book, Tag},
  methods: {
    ...mapActions([
      'loadBooks',
      'addBook',
      'removeBook'
    ]),
    /* create a book */
    addBook () {
      let payload = {
        name: this.name
      }
      this.$store.dispatch('addBook', payload)
    },
    /* delete action pressed */
    delBook (id) {
      this.$store.dispatch('removeBook', id)
    },
    notesByTag (id) {
      return this.$store.dispatch('notesByTag', id)
    },
    notesByBook (id) {
      return this.$store.dispatch('notesByBook', id)
    }
  },
  computed: {
    books () {
      return this.$store.getters.books
    },
    tags () {
      return this.$store.getters.tags
    }
  },
  created () {
    this.$store.dispatch('loadTags')
    this.$store.dispatch('loadBooks')
  }
}
</script>
