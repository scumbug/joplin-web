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
            <h5>Books
                <a class="btn-sm btn-primary" data-toggle="collapse" href="#NewBook" role="button" aria-expanded="false" aria-controls="NewBook">New</a>
                <div class="collapse" id="NewBook">
                    <form @submit.prevent="newFolder">
                        <div class="form-group">
                            <input type="text" v-model="folder" class="form-control" id="folder" placeholder="Book name">
                        </div>
                    </form>
                </div>
            </h5>
            <books></books>
            <h5>Tags
                <a class="btn-sm btn-primary" data-toggle="collapse" href="#NewTag" role="button" aria-expanded="false" aria-controls="NewTag">New</a>
                <div class="collapse" id="NewTag">
                    <form @submit.prevent="newTag">
                        <div class="form-group">
                            <input type="text" v-model="tag" class="form-control" id="tag" placeholder="Name">
                        </div>
                    </form>
                </div>
            </h5>
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

import typesFolders from './modules/folders/types'
import typesTags from './modules/tags/types'

export default {
  components: { Navbar, Books, Tags, Notes, TakeNote },
  data () {
    return {
      folder: '',
      tag: ''
    }
  },
  methods: {
    newFolder (folder) {
      let payload = {
        'title': this.folder
      }
      this.$store.dispatch('folders/' + typesFolders.FOLDER_CREATE, payload)
      this.$store.dispatch('folders/' + typesFolders.FOLDER_FETCH_ALL)
      this.folder = ''
    },
    newTag (tag) {
      let payload = {
        'title': this.tag
      }
      this.$store.dispatch('tags/' + typesTags.TAG_CREATE, payload)
      this.$store.dispatch('tags/' + typesTags.TAG_FETCH_ALL)
      this.tag = ''
    }
  }

}
</script>
