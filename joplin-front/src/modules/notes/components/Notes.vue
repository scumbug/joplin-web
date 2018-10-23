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
    <infinite-loading @infinite="infiniteHandler" ref="infiniteLoading">
        <span slot="no-results">no notes found</span>
        <span slot="no-more">no more notes</span>
    </infinite-loading>
  </div>
</template>

<script>
import axios from 'axios'
import InfiniteLoading from 'vue-infinite-loading'
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
      page: 0
    }
  },
  components: { Note, Task, InfiniteLoading },
  methods: {
    infiniteHandler ($state) {
      let params = {}
      // params.notebook = this.$store.state.folders.folder.title

      if ((this.$store.state.notes.notes.length / 20) > 0) {
        this.page = (this.$store.state.notes.notes.length / 20) + 1
      }
      if (this.page > 0) {
        params.page = this.page
      }
      /*
      if (this.q !== '') {
        params.q = this.q
        params.page = this.page
      }
      */
      axios.get('http://127.0.0.1:8001/api/jw/notes/', {
        params: params
      }).then((res) => {
        if (res.data.count > 0) {
          let notes = this.$store.state.notes.notes.concat(res.data.results)
          this.$store.dispatch('notes/' + types.NOTE_FETCH_PAGE, notes)
          // notes = this.$store.state.notes.notes.concat(res.data.results)
          $state.loaded()
          if (this.$store.state.notes.notes.count / 20 === 10) {
            $state.complete()
          }
        } else {
          $state.complete()
        }
      })
    },
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
  mounted () {
    this.$nextTick(() => {
      this.$refs.infiniteLoading.$emit('$InfiniteLoading:reset')
    })
  },
  created () {
    // this.$store.dispatch('notes/' + types.NOTE_FETCH_ALL)
  }
}
</script>
