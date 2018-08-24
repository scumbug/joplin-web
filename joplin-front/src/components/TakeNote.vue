<template>
    <div class="col-7">
      <form method="post" class="form-horizontal" @submit.prevent="doNote" @keydown="errors.clear($event.target.title)">
          <div class="form-group">
              <input placeholder="no title" class="form-control" name="title" id="title" v-model="note.title"/>
              <span class="help is-danger" v-if="errors.has('title')" v-text="errors.getError('title')"></span>
          </div>
          <div class="form-group">
              <span class="select">
              <select v-model="note.book" class="form-control">
                  <option v-for="book in books" :key="book.id" :value="book.id">{{ book.title }}</option>
              </select>
              </span>
              <span class="help is-danger" v-if="errors.has('book')" v-text="errors.getError('book')"></span>
          </div>
          <div>
          <button v-if="note.id" class="btn btn-danger" :disabled="errors.any()" @click="removeNote(note.id)">Delete this note ?</button>
          </div>
          <div class="form-group">
            <textarea v-model="note.body" @input="updateMarkdown"></textarea>
            <span class="help is-danger" v-if="errors.has('body')" v-text="errors.getError('body')"></span>
          </div>
          <div class="form-group">
            <button class="btn btn-primary" :disabled="errors.any()">Save</button>
          </div>
          <p>preview</p>
          <div v-html="compiledMarkdown"></div>
      </form>
    </div>
</template>

<script>
/* errors class */
import Errors from '../core/Errors'
let marked = require('marked')
let _ = require('lodash')
// import Ckeditor from 'vue-ckeditor2'

export default {
  data () {
    return {
      body: '',
      books: this.$store.getters.books,
      errors: new Errors()
    }
  },
  methods: {
    doNote () {
      if (this.id === 0 || this.id === undefined) {
        this.addNote()
      } else {
        this.updateNote(this.$data)
      }
    },
    /* new note button pressed */
    newNote () {
      this.note = {}
    },
    /* create a note */
    addNote () {
      let payload = {
        title: this.title,
        body: this.body,
        parent: this.book,
        tag: this.tag
      }
      this.$store.dispatch('addNote', payload)
    },
    /* update the note */
    updateNote (note) {
      this.$store.dispatch('updateNote', note)
    },
    /* delete action pressed */
    removeNote (id) {
      this.$store.dispatch('removeNote', id)
    },
    updateMarkdown: _.debounce(function (e) {
      this.note.body = e.target.value
    }, 300)
  },
  computed: {
    compiledMarkdown () {
      console.log('BODY ' + this.body)
      return marked(this.body, { sanitize: true })
    },
    note: {
      get () {
        return this.$store.state.note
      },
      set (value) {
      }
    }
  }
}
</script>
