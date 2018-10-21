<template>
  <div>
    <h5>{{ this.title }}</h5>
    <ul class="nav nav-tabs">
      <li class="nav-item">
        <a class="nav-link active" href="#notes" data-toggle="tab" role="tab">Notes</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#tasks" data-toggle="tab" role="tab">Tasks</a>
      </li>
    </ul>
    <div class="tab-content">
      <div class="tab-pane fade show active" id="notes" role="tabpanel">
        <ul class="list-group">
          <a v-for="note in this.getNotes" :key="note.id" href="#" @click="editNote(note)">
            <div v-if="note.todo_completed == 1" class="card text-success">
              <div class="card-body">
                <p class="card-text">{{ note.title }}</p>
                <p class="card-text">
                  <small class="text-muted">created: {{ moment(note.created_time).format('lll') }}</small>
                  <small v-if="note.todo_due > 0" class="text-muted"> due: {{ moment(note.todo_due).format('lll') }}</small>
                </p>
              </div>
            </div>
            <div v-else-if="note.is_todo == 1 && note.todo_due > 0" class="card text-warning">
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
      <div class="tab-pane fade" id="tasks" role="tabpanel">
        <ul class="list-group">
          <a v-for="note in this.getTasks" :key="note.id" href="#" @click="editNote(note)">
            <Task v-bind:note='note'/>
          </a>
          <a v-for="note in this.getTasksDue" :key="note.id" href="#" @click="editNote(note)">
            <Task v-bind:note='note'/>
          </a>
          <a v-for="note in this.getTasksCompleted" :key="note.id" href="#" @click="editNote(note)">
            <Task v-bind:note='note'/>
          </a>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
// note content
import Note from './Note.vue'
import Task from './Task.vue'

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
  components: { Note, Task },
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
    getTasks () {
      return this.$store.state.notes.notes.filter(note => note.is_todo === 1 && note.todo_completed === 0)
    },
    getTasksDue () {
      return this.$store.state.notes.notes.filter(note => note.is_todo === 1 && note.todo_due > 0)
    },
    getTasksCompleted () {
      return this.$store.state.notes.notes.filter(note => note.todo_completed === 1)
    },
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
