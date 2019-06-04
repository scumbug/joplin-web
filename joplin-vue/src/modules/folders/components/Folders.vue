<template>
  <b-list-group>
    <b-list-group-item class="justify-content-between align-items-center"
      v-for="folder in this.getParentFolders"
      :key="folder.id">
      <a href="#" @click="notesByFolder(folder)">{{ folder.title }}</a>&nbsp;
      <b-badge pill>{{ folder.nb_notes }}</b-badge>
      <folder :parent_folder="folder"/>
    </b-list-group-item>
  </b-list-group>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'

import Folder from './Folder'

import getters from '../getters'
import actions from '../actions'
import types from '../types'
import typesNote from '../../notes/types'
import typesTag from '../../tags/types'

const namespace = 'folders'
const { mapGetters, mapActions } = createNamespacedHelpers(namespace)

export default {
  data () {
    return {
      selection: []
    }
  },
  components: { Folder },
  methods: {
    notesByFolder (folder) {
      let tag = {}
      this.$store.dispatch('folders/' + types.FOLDER_FETCH, folder)
      this.$store.dispatch('tags/' + typesTag.TAG_FETCH, tag)
      this.$store.dispatch('notes/' + typesNote.NOTE_FETCH_FOLDER, folder)
    },
    ...mapActions(Object.keys(actions))
  },
  computed: {
    ...mapGetters(Object.keys(getters)),

    getParentFolders () {
      return this.$store.state.folders.folders.filter(folder => folder.parent_id === '')
    }
  },
  created () {
    this.$store.dispatch('folders/' + types.FOLDER_FETCH_ALL)
  }
}
</script>
