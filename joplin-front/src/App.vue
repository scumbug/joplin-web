<template>
  <div>
      <div class="container-fluid">
        <div class="row">
          <div class="col">
            <navbar></navbar>
          </div>
        </div>
      </div>
      <div class="row">
          <div class="col-2">
            <books></books>
            <tags></tags>
          </div>
          <div class="col-5">
            <notes></notes>
          </div>
          <div class="col-5">
            <take-note></take-note>
          </div>
      </div>
  </div>
</template>

<script>
import Navbar from './components/NavBar.vue'
import Books from './modules/folders/components/Books.vue'
import Tags from './modules/tags/components/Tags.vue'
import Notes from './modules/notes/components/Notes.vue'
import TakeNote from './modules/notes/components/TakeNote.vue'
export default {
  components: { Navbar, Books, Tags, Notes, TakeNote }
}
</script>
