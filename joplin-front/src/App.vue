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
            <h5>Books</h5>
            <books></books>
            <h5>Tags</h5>
            <tags></tags>
          </div>
          <div class="col-3">
            <notes></notes>
          </div>
          <div class="col-7">
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
