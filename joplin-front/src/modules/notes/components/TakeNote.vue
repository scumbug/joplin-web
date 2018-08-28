<template>
  <form method="post" class="form-horizontal" @submit.prevent="doNote" @keydown="errors.clear($event.target.title)">
      <div class="form-group">
          <input placeholder="no title" class="form-control" name="title" id="title" :value="note.title"/>
          <span class="help is-danger" v-if="errors.has('title')" v-text="errors.getError('title')"></span>
      </div>
      <div class="form-group">
          <span class="select">
          <select :value="note.folder" class="form-control">
              <option v-for="folder in this.getFolders2" :key="folder.id" :value="folder.id">{{ folder.title }}</option>
          </select>
          </span>
          <span class="help is-danger" v-if="errors.has('book')" v-text="errors.getError('book')"></span>
      </div>
      <div>
        <button v-if="note.id" class="btn btn-danger" @click="removeNote(note.id)">Delete this note ?</button>
      </div>
      <div class="form-group">
        <vue-ckeditor v-model="note.body" :config="config" />
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

import VueCkeditor from 'vue-ckeditor2'

const namespace = 'notes'
const { mapGetters, mapActions } = createNamespacedHelpers(namespace)

export default {
  components: { VueCkeditor },
  data () {
    return {
      id: 0,
      folders: {},
      errors: new Errors(),
      config: {
        toolbar: [
          { name: 'document', items: [ 'Source', '-', 'Preview', 'Print', '-' ] },
          { name: 'clipboard', items: [ 'Cut', 'Copy', 'Paste', 'PasteText', '-', 'Undo', 'Redo' ] },
          { name: 'editing', items: [ 'Find', 'Replace', '-', 'SelectAll', '-', 'Scayt' ] },
          '/',
          { name: 'basicstyles', items: [ 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'CopyFormatting', 'RemoveFormat' ] },
          { name: 'paragraph', items: [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language' ] },
          { name: 'links', items: [ 'Link', 'Unlink', 'Anchor' ] },
          { name: 'insert', items: [ 'Image', 'Table', 'HorizontalRule', 'Smiley' ] },
          '/',
          { name: 'styles', items: [ 'Styles', 'Format', 'Font', 'FontSize' ] },
          { name: 'colors', items: [ 'TextColor', 'BGColor' ] },
          { name: 'tools', items: [ 'Maximize', 'ShowBlocks' ] }
        ],
        font_names: 'OpenDyslexic;Arial;Comic Sans MS;Courier New;Lucida Sans Unicode;Tahoma;Times New Roman;Trebuchet MS;Verdana;',
        height: '340px'
      },
      configs: {
        spellChecker: false,
        status: false,
        initialValue: '',
        renderingConfig: {
          codeSyntaxHighlighting: true
          // highlightingTheme: 'atom-one-light',
        },
        autofocus: true,
        autosave: {
          enabled: true,
          uniqueId: 'OroUniqueID',
          delay: 1000
        }
      }
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
        title: this.note.title,
        body: this.note.body,
        parent: this.note.folder,
        tag: this.note.tag
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
    ...mapActions(Object.keys(actions))
  },
  computed: {
    note: {
      get () {
        return this.$store.state.notes.note
      },
      set (value) {
      }
    },
    ...mapGetters(Object.keys(getters))
  },
  mounted () {
    return Object.assign({}, this.$store.state.notes.note)
  }
}
</script>
