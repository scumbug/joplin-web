<template>
  <div>
    <b-navbar toggleable="md" variant="light">
      <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

      <b-navbar-brand href="#">Joplin Web</b-navbar-brand>

      <b-collapse is-nav id="nav_collapse">

        <b-navbar-nav>
          <b-nav-item href="#" @click="getNotes()">Home</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-btn size="sm" class="my-2 my-sm-0" @click="newNote()" variant="outline-primary"><i class="fas fa-plus-circle"></i> New note</b-btn>
          &nbsp;
          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" type="text" v-model="q" @keyup.enter="searchNote()" placeholder="Search"/>
            <b-button size="sm" class="my-2 my-sm-0" variant="outline-success" type="submit">Search</b-button>
          </b-nav-form>
        </b-navbar-nav>

      </b-collapse>
    </b-navbar>

  </div>
</template>

<script>
import typesFolders from '../modules/folders/types'
import typesNotes from '../modules/notes/types'
import typesTags from '../modules/tags/types'

export default {
  data () {
    return {
      q: ''
    }
  },
  methods: {
    searchNote () {
      // this.emit('searchNote', this.q)
    },
    getNotes () {
      this.$store.dispatch('folders/' + typesFolders.FOLDER_FETCH_ALL)
      this.$store.dispatch('notes/' + typesNotes.NOTE_FETCH_ALL)
      this.$store.dispatch('tags/' + typesTags.TAG_FETCH_ALL)
    },
    newNote () {
      // clean the form to add a new note
      this.$store.dispatch('notes/' + typesNotes.NOTE_NEW)
    }
  }
}
</script>
