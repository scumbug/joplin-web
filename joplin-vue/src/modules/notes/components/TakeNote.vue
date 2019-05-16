<template>
  <form method="post" class="form-horizontal" @submit.prevent="doNote">
    <b-alert v-if="updated == 1" v-model="updated" variant="success" show>Update done</b-alert>
    <b-alert v-if="updated == 0" v-model="updated" variant="danger">Update failed</b-alert>
    <div class="input-group input-group-sm mb-3">
      <b-form-input v-model="title"
                    type="text"
                    name="title"
                    id="title"
                    placeholder="Enter your title">
      </b-form-input>
      <span class="help is-danger" v-if="errors.has('title')" v-text="errors.getError('title')"></span>
      <div class="input-group-append">
        <b-button v-if="id" size="sm" variant="danger" @click="removeNote(id)"><i class="fas fa-trash"></i> Delete this note ?
        </b-button>
      </div>
    </div>
    <div class="form-group row">
      <div class="col-sm-2">
      <label v-if="is_todo==1" class="btn btn-secondary btn-sm active"><i class="fas fa-tasks"></i> Tasks ?
        <input name="is_todo" id="is_todo" v-model="is_todo" type="checkbox" checked autocomplete="off"/>
      </label>
      <label v-if="is_todo==0" class="btn btn-secondary btn-sm"><i class="fas fa-tasks"></i> Tasks ?
        <input name="is_todo" id="is_todo" v-model="is_todo" type="checkbox" autocomplete="on"/>
      </label>
      </div>
      <div class="col-sm-6">
        <b-form-input v-model="tag"
                      type="text"
                      name="tag"
                      id="tag"
                      placeholder="tags, tags">
        </b-form-input>
      </div>
      <div class="col-sm-4">
        <div class="input-group-prepend">
          <span class="text-muted">Created: {{ moment(created_time).format('lll') }}</span>&nbsp;
          <b-btn id="note-info" size="sm" variant="secondary"><i class="fas fa-info-circle"></i></b-btn>
          <b-popover target="note-info" triggers="hover focus">
            <template slot="title">Note details</template>
            <ul>
              <li v-if="author !== ''">Author: {{ author }}</li>
              <li v-else>Author n/a</li>
              <li v-if="source_url !== ''">URL: {{ source_url }}</li>
              <li v-else>URL n/a</li>
              <li>Date
                <ul>
                  <li v-if="created_time > 0">Created: {{ moment(created_time).format('lll') }}</li>
                  <li v-if="updated_time > 0">Updated: {{ moment(updated_time).format('lll') }}</li>
                </ul>
              </li>
              <li>Geo location
                <ul>
                <li>Latitude {{ latitude }}</li>
                <li>Longitude {{ longitude }}</li>
                <li>Altitude {{ altitude }}</li>
                </ul>
              </li>
              <li>Tasks
                <ul>
                  <li v-if="todo_completed > 0">Todo Completed: {{ moment(todo_completed).format('lll') }}</li>
                  <li v-else>Todo Competed: n/a</li>
                  <li v-if="todo_due > 0">Todo Due: {{ moment(todo_due).format('lll') }}</li>
                  <li v-else>Todo Due: n/a</li>
                </ul>
              </li>
              <li>Source
                <ul>
                  <li>Source: {{ source }}</li>
                  <li>Source Application: {{ source_application }}</li>
                  <li>ID: {{ id }}</li>
                </ul>
              </li>
            </ul>
          </b-popover>
        </div>
      </div>
    </div>
    <div class="form-group">
      <div class="input-group input-group-sm mb-3">
        <div class="input-group-prepend">
          <label class="input-group-text" for="inputGroupSelect01"><i class="fas fa-folder-open"></i> Folder</label>
        </div>
        <b-form-select v-model="parent_id" id="parent_id" name="parent_id" >
          <option v-for="folder in this.getFolders2" :key="folder.id" :value="folder.id">{{ folder.title }}</option>
        </b-form-select>
      </div>
      <span class="help is-danger" v-if="errors.has('folder')" v-text="errors.getError('folder')"></span>
    </div>
    <div class="form-group row">
      <div class="col-sm-6">
        <b-form-textarea id="body"
                         v-model="body"
                         placeholder="Enter something"
                         :rows="25"
                         :max-rows="40"
                         @input="updateBody">
        </b-form-textarea>
        <span class="help is-danger" v-if="errors.has('body')" v-text="errors.getError('body')"></span><br/>
        <b-alert v-if="updated == 1" v-model="updated" variant="success" show>Update done</b-alert>
        <b-alert v-if="updated == 0" v-model="updated" variant="danger">Update failed</b-alert>
        <button class="btn btn-primary" :disabled="errors.any()">
          <span><i class="fas fa-save"></i> Save</span>
        </button>
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
      urlResources: 'http://127.0.0.1:8001/static',
      updated: -1,
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
        'is_todo': (this.is_todo ? 1 : 0),
        'tag': this.tag
      }
      this.$store.dispatch('notes/' + types.NOTE_CREATE, payload)
    },
    /* update the note */
    updateNote () {
      // payload
      let payload = {
        'id': this.id,
        'title': this.title,
        'body': this.body,
        'parent_id': this.parent_id,
        'tag': this.tag,
        'is_todo': (this.is_todo ? 1 : 0)
      }
      // push the data
      this.$store.dispatch('notes/' + types.NOTE_CHANGE, payload)
        .then((res) => {
          this.updated = 1
        })
        // eslint-disable-next-line
        .catch((error) => {
          this.updated = 0
        })
    },
    /* delete action pressed */
    removeNote () {
      this.$store.dispatch('notes/' + types.NOTE_REMOVE, this.id)
    },
    // translate markdown to html
    updateBody: _.debounce(function (e) {
      // spot image markdown
      // eslint-disable-next-line
      let re = /\!\[(.*)\.(\w+)\]\(:\/(.*)\)/g
      // image markdown : ![image name.extension](:/resource_id)
      // becomes
      // image markdown : ![image name.extension](http://127.0.0.1:8001/static/resource_id.extension)
      // add the URL to access to the image from the back http service
      this.body = e.replace(re, '![$1.$2](' + this.urlResources + '/$3.$2)')
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

    // mapFields('namespace' {input name: 'object.field', ... })
    // this allow to set parent_id with a the id of the object of the object
    ...mapFields('notes', {
      id: 'note.id',
      title: 'note.title',
      body: 'note.body',
      is_todo: 'note.is_todo',
      parent_id: 'note.parent.id',
      created_time: 'note.created_time',
      updated_time: 'note.updated_time',
      todo_completed: 'note.todo_completed',
      todo_due: 'note.todo_due',
      source_url: 'note.source_url',
      author: 'note.author',
      latitude: 'note.latitude',
      longitude: 'note.longitude',
      altitude: 'note.altitude',
      source: 'note.source',
      source_application: 'note.source_application',
      tag: 'tag'
    })
  }
}
</script>
