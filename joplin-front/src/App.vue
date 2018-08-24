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
          <books></books>
          <notes></notes>
          <take-note></take-note>
      </div>
  </div>
</template>

<script>
import Navbar from './components/NavBar.vue'
import Books from './components/Books.vue'
import Notes from './components/Notes.vue'
import TakeNote from './components/TakeNote.vue'
export default {
  components: { Navbar, Books, Notes, TakeNote }
}
</script>
