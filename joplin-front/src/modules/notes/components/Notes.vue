<template>
  <div>
    <h5>{{this.title}}</h5>
    <ul class="list-group">
      <note v-for="note in this.getNotes" :key="note.id">
      <a href="#" @click="editNote(note)">{{ note.title }}</a>
      </note>
    </ul>
  </div>

</template>

<script>
// note content
import Note from './Note.vue'

import { createNamespacedHelpers } from 'vuex'

import getters from '../getters'
import actions from '../actions'
import types from '../types'

const namespace = 'notes'
const { mapGetters, mapActions } = createNamespacedHelpers(namespace)

export default {
  data () {
    return {
    }
  },
  components: { Note },
  methods: {
    editNote (note) {
      this.$store.dispatch('notes/' + types.NOTE_SET, note)
    },
    delNote (id) {
      this.$store.dispatch('notes/' + types.NOTE_REMOVE, id)
    },
    searchNote () {
    },
    ...mapActions(Object.keys(actions))
  },
  computed: {
    ...mapGetters(Object.keys(getters)),
    title: {
      get () {
        if (this.$store.state.folders.folder.title !== undefined) {
          return 'Notes > Folder > ' + this.$store.state.folders.folder.title
        } else if (this.$store.state.tags.tag.title !== undefined) {
          return 'Notes > Tag > ' + this.$store.state.tags.tag.title
        }
        return 'All notes'
      }
    }
  },
  created () {
    this.$store.dispatch('notes/' + types.NOTE_FETCH_ALL)
  }
}
</script>
