<template>
  <div>
    <h5 v-html="this.title"></h5>
    <b-tabs>
      <b-tab title="notes" active>
        <b-list-group>
          <a v-for="note in this.getNotes" :key="note.id" href="#" @click="editNote(note)">
            <b-card :title="note.title" v-if="note.todo_completed == 1" border-variant="success">
              <p class="card-text">
                <small class="text-muted">created: {{ moment(note.created_time).format('lll') }}</small>
                <small v-if="note.todo_due > 0" class="text-muted"> due: {{ moment(note.todo_due).format('lll') }}</small>
              </p>
            </b-card>
            <b-card :title="note.title" v-else-if="note.is_todo == 1 && note.todo_due > 0" border-variant="warning">
              <p class="card-text">
                <small class="text-muted">created: {{ moment(note.created_time).format('lll') }}</small>
                <small v-if="note.todo_due > 0" class="text-muted"> due: {{ moment(note.todo_due).format('lll') }}</small>
              </p>
            </b-card>
            <b-card :title="note.title" v-else>
              <p class="card-text">
                <small class="text-muted">created: {{ moment(note.created_time).format('lll') }}</small>
                <small v-if="note.todo_due > 0" class="text-muted"> due: {{ moment(note.todo_due).format('lll') }}</small>
              </p>
            </b-card>
          </a>
        </b-list-group>
      </b-tab>
      <b-tab title="tasks">
        <b-list-group>
          <a v-for="note in this.getTasks" :key="note.id" href="#" @click="editNote(note)">
            <Task v-bind:note='note'/>
          </a>
          <a v-for="note in this.getTasksDue" :key="note.id" href="#" @click="editNote(note)">
            <Task v-bind:note='note'/>
          </a>
          <a v-for="note in this.getTasksCompleted" :key="note.id" href="#" @click="editNote(note)">
            <Task v-bind:note='note'/>
          </a>
        </b-list-group>
      </b-tab>
    </b-tabs>
    <infinite-loading @infinite="infiniteHandler" ref="infiniteLoading">
        <span slot="no-more">No more message</span>
        <span slot="no-results">No results message</span>
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
      let pageSize = 20
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
      axios.get('/api/jw/notes/', {
        params: params
      }).then((res) => {
        if (res.data.count > 0) {
          // concat the result from the backend with the store
          let notes = this.$store.state.notes.notes.concat(res.data.results)
          // update the store
          this.$store.dispatch('notes/' + types.NOTE_FETCH_PAGE, notes)
          $state.loaded()
          if (notes.count / pageSize === 10) {
            $state.complete()
          }
        } else {
          $state.complete()
        }
      })
    },
    editNote (note) {
      this.$store.dispatch('notes/' + types.NOTETAG_SET, note)
      this.$store.dispatch('notes/' + types.NOTE_SET, note)
    },
    delNote (id) {
      this.$store.dispatch('notes/' + types.NOTE_REMOVE, id)
    },
    searchNote () {
      // @TODO
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
          return '<i class="fas fa-folder-open"></i> From Book / ' + this.$store.state.folders.folder.title
        } else if (this.$store.state.tags.tag.title !== undefined) {
          return '<i class="fas fa-tags"></i> From Tag / ' + this.$store.state.tags.tag.title
        }
        return 'All notes'
      }
    }
  },
  mounted () {
    this.$nextTick(() => {
      this.$refs.infiniteLoading.$emit('$InfiniteLoading:reset')
    })
  }
}
</script>
