<template>
  <div>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Joplin Web</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item"><a class="nav-link" href="#" @click="getNotes()">Home</a></li>
      </ul>
      <ul class="navbar-nav mr-auto">
        <li class="nav-item"><button class="btn btn-success" @click="newNote()">Note</button></li>
        <li class="nav-item">&nbsp;<button class="btn btn-success" @click="newFolder()">Book</button></li>
      </ul>
      <form class="form-inline my-2 my-lg-0">
        <input class="form-control  mr-sm-2" type="search" v-model="q" @keyup.enter="searchNote()" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </form>
    </div>
  </nav>
  </div>
</template>

<script>
import typesFolders from '../modules/folders/types'
import typesNotes from '../modules/notes/types'
import typesTags from '../modules/tags/types'

export default {
  props: ['noteName', 'folderName'],
  data () {
    return {
      q: ''
    }
  },
  methods: {
    newNote () {
      this.$store.dispatch('notes/' + typesNotes.NOTE_NEW)
    },
    newFolder () {
      // this.emit('newFolder')
    },
    searchNote () {
      // this.emit('searchNote', this.q)
    },
    getNotes () {
      this.$store.dispatch('folders/' + typesFolders.FOLDER_FETCH_ALL)
      this.$store.dispatch('notes/' + typesNotes.NOTE_FETCH_ALL)
      this.$store.dispatch('tags/' + typesTags.TAG_FETCH_ALL)
    }
  }
}
</script>
