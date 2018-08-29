<template>
  <div>
    <ul class="list-group">
    <tag v-for="tag in this.getTags" :key="tag.id">
      <a href="#" @click="notesByTag(tag.id)">{{ tag.title }}</a><tags-counter v-bind:tag="tag.id"></tags-counter>
    </tag>
    </ul>
  </div>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'

import Tag from './Tag'

import getters from '../getters'
import actions from '../actions'
import types from '../types'
import typesNote from '../../notes/types'
import TagsCounter from './TagsCounter'

const namespace = 'tags'
const { mapGetters, mapActions } = createNamespacedHelpers(namespace)

export default {
  data () {
    return {
    }
  },
  components: { Tag, TagsCounter },
  methods: {
    ...mapActions(Object.keys(actions)),
    notesByTag (tag) {
      this.$store.dispatch('notes/' + typesNote.NOTE_FETCH_TAG, tag)
    }
  },
  computed: {
    ...mapGetters(Object.keys(getters))
  },
  created () {
    this.$store.dispatch('tags/' + types.TAG_FETCH_ALL)
  }
}
</script>
