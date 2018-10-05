<template>
  <div>
    <h5>{{ this.title }}</h5>
    <ul class="list-group">
      <a v-for="note in this.getNotes" :key="note.id" href="#" @click="editNote(note)">
        <div v-if="note.is_todo==1" class="card text-success">
          <div class="card-body">
            <p class="card-text">{{ note.title }}</p>
            <p class="card-text">
              <small class="text-muted">created: {{ moment(note.created_time).format('lll') }}</small>
              <small v-if="note.todo_due > 0" class="text-muted"> due: {{ moment(note.todo_due).format('lll') }}</small>
            </p>
          </div>
        </div>
        <div v-else class="card">
          <div class="card-body">
            <p class="card-text">{{ note.title }}</p>
            <p class="card-text">
              <small class="text-muted">created: {{ moment(note.created_time).format('lll') }}</small>
              <small v-if="note.todo_due > 0" class="text-muted"> due: {{ moment(note.todo_due).format('lll') }}</small>
            </p>
          </div>
        </div>
      </a>
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
          return 'From Book / ' + this.$store.state.folders.folder.title
        } else if (this.$store.state.tags.tag.title !== undefined) {
          return 'From Tag / ' + this.$store.state.tags.tag.title
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
