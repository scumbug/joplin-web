<template>
  <form method="post" class="form-horizontal" @submit.prevent="doNote" @keydown="errors.clear($event.target.title)">
      <div class="form-group">
          <input placeholder="no title" class="form-control" name="title" id="title" v-model="title"/>
          <span class="help is-danger" v-if="errors.has('title')" v-text="errors.getError('title')"></span>
      </div>
      <div class="form-group">
          <span class="select">
          <select v-model="folder" class="form-control">
              <option v-for="folder in this.getFolders2" :key="folder.id" :value="folder.id">{{ folder.title }}</option>
          </select>
          </span>
          <span class="help is-danger" v-if="errors.has('book')" v-text="errors.getError('book')"></span>
      </div>
      <div>
      <button v-if="id" class="btn btn-danger" @click="removeNote(id)">Delete this note ?</button>
      </div>
      <div class="form-group">
        <textarea v-model="body" @input="updateMarkdown"></textarea>
        <span class="help is-danger" v-if="errors.has('body')" v-text="errors.getError('body')"></span>
      </div>
      <div class="form-group">
        <button class="btn btn-primary" :disabled="errors.any()">Save</button>
      </div>
      <p>preview</p>
      <div v-html="compiledMarkdown"></div>
  </form>
</template>

<script>
import Errors from '../../../core/Errors'
import { createNamespacedHelpers } from 'vuex'

import getters from '../getters'
import actions from '../actions'
import types from '../types'

let marked = require('marked')
let _ = require('lodash')

const namespace = 'notes'
const { mapGetters, mapActions } = createNamespacedHelpers(namespace)

export default {
  data () {
    return {
      id: 0,
      title: '',
      folder: '',
      body: '',
      folders: {},
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
        parent: this.folder,
        tag: this.tag
      }
      this.$store.dispatch('notes/' + types.NOTE_CREATE, payload)
    },
    /* update the note */
    updateNote (note) {
      this.$store.dispatch('notes/' + types.NOTE_UPDATE, note)
    },
    /* delete action pressed */
    removeNote (id) {
      this.$store.dispatch('notes/' + types.NOTE_REMOVE, id)
    },
    updateMarkdown: _.debounce(function (e) {
      this.note.body = e.target.value
    }, 300),
    ...mapActions(Object.keys(actions))
  },
  computed: {
    compiledMarkdown () {
      return marked(this.body, { sanitize: true })
    },
    note: {
      get () {
        return this.$store.state.note
      },
      set (value) {
      }
    },
    ...mapGetters(Object.keys(getters))
  }
}
</script>
