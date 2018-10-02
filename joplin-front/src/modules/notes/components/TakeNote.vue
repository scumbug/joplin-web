<template>
  <form method="post" class="form-horizontal" @submit.prevent="doNote">
    <div class="input-group input-group-sm mb-3">
      <input placeholder="no title" class="form-control form-control-sm" name="title" id="title" v-model="title"/>
      <span class="help is-danger" v-if="errors.has('title')" v-text="errors.getError('title')"></span>
      <div class="input-group-append">
        <button v-if="id" class="btn btn-danger btn-sm" @click="removeNote(id)" type="button" id="button-addon2">Delete this note ?</button>
      </div>
    </div>
    <div class="form-group">
      <label v-if="is_todo==1" class="btn btn-secondary btn-sm active">
        <input name="is_todo" id="is_todo" v-model="is_todo" type="checkbox" checked autocomplete="off"> Tasks ?
      </label>
      <label v-if="is_todo==0" class="btn btn-secondary btn-sm">
        <input name="is_todo" id="is_todo" v-model="is_todo" type="checkbox" autocomplete="on"> Tasks ?
      </label>
    </div>
    <div class="form-group">
      <div class="input-group input-group-sm mb-3">
        <div class="input-group-prepend">
          <label class="input-group-text" for="inputGroupSelect01">Folder</label>
        </div>
        <select v-model="parent_id" class="custom-select" id="inputGroupSelect01">
          <option v-for="folder in this.getFolders2" :key="folder.id" :value="folder.id">{{ folder.title }}</option>
        </select>
      </div>
      <span class="help is-danger" v-if="errors.has('folder')" v-text="errors.getError('folder')"></span>
    </div>
    <div class="form-group row">
      <div class="col-sm-6">
        <textarea class="form-control form-control-sm" rows="25" v-model="body" @input="updateBody"></textarea>
        <span class="help is-danger" v-if="errors.has('body')" v-text="errors.getError('body')"></span><br/>
        <button class="btn btn-primary" :disabled="errors.any()">Save</button>
      </div>
      <div class="col-sm-6">
        <div v-html="compiledMarkdown"></div>
      </div>
    </div>
  </form>
</template>

<script>
import Errors from '../../../core/Errors'
import { createNamespacedHelpers } from 'vuex'

import getters from '../getters'
import actions from '../actions'
import types from '../types'

// import { mapFields } from 'vuex-map-fields'
import { createHelpers } from 'vuex-map-fields'

import _ from 'lodash'
let marked = require('marked')

const namespace = 'notes'
const { mapGetters, mapActions } = createNamespacedHelpers(namespace)

const { mapFields } = createHelpers({
  getterType: 'getNoteField',
  mutationType: 'updateNoteField'
})

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
      if (this.id === undefined || this.id === 0) {
        this.addNote()
      } else {
        this.updateNote()
      }
    },
    /* create a note */
    addNote () {
      let payload = {
        'title': this.title,
        'body': this.body,
        'parent_id': this.parent_id,
        'is_todo': (this.is_todo ? 1 : 0)
      }
      this.$store.dispatch('notes/' + types.NOTE_CREATE, payload)
    },
    /* update the note */
    updateNote () {
      // payload
      console.log(this.id)
      let payload = {
        'id': this.id,
        'title': this.title,
        'body': this.body,
        'parent_id': this.parent_id,
        'is_todo': (this.is_todo ? 1 : 0)
      }
      // push the data
      this.$store.dispatch('notes/' + types.NOTE_CHANGE, payload)
    },
    /* delete action pressed */
    removeNote () {
      this.$store.dispatch('notes/' + types.NOTE_REMOVE, this.id)
    },
    // translate markdown to html
    updateBody: _.debounce(function (e) {
      this.input = e.target.value
    }, 300),
    ...mapActions(Object.keys(actions))
  },
  // load the data of the store into the form for each input
  computed: {
    compiledMarkdown: function () {
      let body = ''
      if (this.$store.state.notes.note.body !== undefined) {
        body = this.$store.state.notes.note.body
      }
      return marked(body, { sanitize: true })
    },
    ...mapGetters(Object.keys(getters)),

    // mapFileds('namespace' {input name: 'object.field', ... })
    // this allow to set parent_id with a the id of the object of the object
    ...mapFields('notes', {
      id: 'note.id',
      title: 'note.title',
      body: 'note.body',
      is_todo: 'note.is_todo',
      parent_id: 'note.parent.id'
    })
  }
  /*
  mounted () {
    return Object.assign({}, this.$store.state.notes.note)
  }
  */
}
</script>
