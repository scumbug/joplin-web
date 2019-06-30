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
        <div role="tablist">
          <b-card no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
              <b-button block href="#" v-b-toggle.folders variant="info"><i class="fas fa-folder-open"></i>  Folders</b-button>
            </b-card-header>
            <b-collapse id="folders" visible accordion="my-folders" role="tabpanel">
              <b-card-body>
                <b-btn v-b-toggle.newfolder variant="primary" size="sm"><i class="fas fa-plus-circle"></i> New folder </b-btn>
                   <b-collapse id="newfolder" class="mt-2">
                    <form @submit.prevent="newFolder">
                       <div class="form-group">
                         <input type="text" v-model="folder" class="form-control" id="folder" placeholder="Folder name">
                        </div>
                    </form>
                  </b-collapse>
                <b-card-text><folders></folders></b-card-text>
              </b-card-body>
            </b-collapse>
          </b-card>
          <b-card no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
              <b-button block href="#" v-b-toggle.tags variant="info"><i class="fas fa-tags"></i> Tags</b-button>
            </b-card-header>
            <b-collapse id="tags" visible accordion="my-tags" role="tabpanel">
              <b-card-body>
                <b-btn v-b-toggle.newtag variant="primary" size="sm"><i class="fas fa-plus-circle"></i> New tag </b-btn>
                <b-collapse id="newtag" class="mt-2">
                  <form @submit.prevent="newTag">
                    <div class="form-group">
                      <input type="text" v-model="tag" class="form-control" id="tag" placeholder="Tag name">
                    </div>
                  </form>
                </b-collapse>
                <b-card-text><tags></tags></b-card-text>
              </b-card-body>
            </b-collapse>
          </b-card>
        </div>
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
import Folders from './modules/folders/components/Folders.vue'
import Tags from './modules/tags/components/Tags.vue'
import Notes from './modules/notes/components/Notes.vue'
import TakeNote from './modules/notes/components/TakeNote.vue'

import typesFolders from './modules/folders/types'
import typesTags from './modules/tags/types'

export default {
  components: { Navbar, Folders, Tags, Notes, TakeNote },
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
