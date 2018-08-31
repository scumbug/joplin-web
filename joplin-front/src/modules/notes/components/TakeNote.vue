<template>
  <!--form method="post" class="form-horizontal" @submit.prevent="doNote" @keydown="errors.clear($event.target.title)"-->
  <form method="post" class="form-horizontal" @submit.prevent="doNote">
      <div class="form-group">
          <input placeholder="no title" class="form-control" name="title" id="title" :value="title"/>
          <span class="help is-danger" v-if="errors.has('title')" v-text="errors.getError('title')"></span>
      </div>
      <div class="form-group">
        <label v-if="is_todo==1" label class="btn btn-secondary active">
          <input name="is_todo" id="is_todo" :value="is_todo" type="checkbox" checked autocomplete="off"> Tasks ?
        </label>
        <label v-if="is_todo==0" label class="btn btn-secondary">
          <input name="is_todo" id="is_todo" :value="is_todo" type="checkbox" autocomplete="on"> Tasks ?
        </label>
      </div>
      <div class="form-group">
          <span class="select">
          <select :value="folder" class="form-control">
              <option v-for="folder in this.getFolders2" :key="folder.id" :value="folder.id">{{ folder.title }}</option>
          </select>
          </span>
          <span class="help is-danger" v-if="errors.has('folder')" v-text="errors.getError('folder')"></span>
      </div>
      <div>
        <button v-if="id" class="btn btn-danger" @click="removeNote(id)">Delete this note ?</button>
      </div>
      <div class="form-group">
        <textarea class="form-control" :value="body"></textarea>
        <span class="help is-danger" v-if="errors.has('body')" v-text="errors.getError('body')"></span>
      </div>
      <div class="form-group">
        <button class="btn btn-primary" :disabled="errors.any()">Save</button>
      </div>
  </form>
</template>

<script>
import Errors from '../../../core/Errors'
import { createNamespacedHelpers } from 'vuex'

import getters from '../getters'
import actions from '../actions'
import types from '../types'

const namespace = 'notes'
const { mapGetters, mapActions } = createNamespacedHelpers(namespace)

export default {
  data () {
    return {
      folders: {},
      errors: new Errors()
    }
  },
  components: { },
  methods: {
    doNote () {
      if (this.id === 0 || this.id === undefined) {
        this.addNote()
      } else {
        this.updateNote()
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
        is_todo: this.is_todo
        // tag_id: this.tag
      }
      this.$store.dispatch('notes/' + types.NOTE_CREATE, payload)
    },
    /* update the note */
    updateNote () {
      // payload
      let payload = {
        id: this.id,
        title: this.title,
        body: this.body,
        parent: this.folder,
        is_todo: this.is_todo
      }
      // push the data
      this.$store.dispatch('notes/' + types.NOTE_CHANGE, payload)
    },
    /* delete action pressed */
    removeNote () {
      this.$store.dispatch('notes/' + types.NOTE_REMOVE, this.note.id)
    },
    ...mapActions(Object.keys(actions))
  },
  // load the data of the store into the form for each input
  computed: {
    id: {
      get () {
        return this.$store.state.notes.note.id
      }
    },
    title: {
      get () {
        return this.$store.state.notes.note.title
      }
    },
    is_todo: {
      get () {
        return this.$store.state.notes.note.is_todo
      }
    },
    folder: {
      get () {
        if (this.id) {
          return this.$store.state.notes.note.parent.id
        }
      }
    },
    body: {
      get () {
        return this.$store.state.notes.note.body
      }
    },
    ...mapGetters(Object.keys(getters))
  },
  mounted () {
    return Object.assign({}, this.$store.state.notes.note)
  }
}
</script>
