<template>
  <b-list-group>
    <b-list-group-item class="d-flew justify-content-between align-items-center"
      v-for="folder in parent_folder"
      :key="folder.id">
      <b-link :to="{ name: 'myFolder', params: { id: folder.title } }"
          replace
          v-slot="{ href, route, navigate, isActive, isExactActive }">
        <a :href="href" @click="notesByFolder(folder)">{{ folder.title }}</a>&nbsp;
        <b-badge pill variant='primary'>{{ folder.nb_notes }}</b-badge>
      </b-link>
      <folder :parent_folder="Object.assign({}, folder.children)"/>
    </b-list-group-item>
  </b-list-group>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'

import getters from '../getters'
import actions from '../actions'
import types from '../types'
import typesNote from '../../notes/types'
import typesTag from '../../tags/types'

const namespace = 'folders'
const { mapGetters, mapActions } = createNamespacedHelpers(namespace)

export default {
  name: 'Folder',
  props: {
    parent_folder: Object
  },
  computed: {
    ...mapGetters(Object.keys(getters))
  },
  methods: {
    notesByFolder (folder) {
      let tag = {}
      this.$store.dispatch('folders/' + types.FOLDER_FETCH, folder)
      this.$store.dispatch('tags/' + typesTag.TAG_FETCH, tag)
      this.$store.dispatch('notes/' + typesNote.NOTE_FETCH_FOLDER, folder)
    },
    ...mapActions(Object.keys(actions))
  }
}

</script>
