<template>
    <div>
        <h3>Tags</h3>
        <div class="articles">
            <ul class="list-group">
                <tag v-for="tag in this.getTags" :key="tag.id">
                    <li class="list-group-item">
                        <a href="#" @click="getNotesByTag(tag.id)">{{ tag.title }}</a>
                    </li>
                </tag>
            </ul>
        </div>
    </div>
</template>

<script>
import Tag from './Tag'

import { createNamespacedHelpers } from 'vuex'

import getters from '../getters'
import actions from '../actions'
import types from '../types'
import typesNote from '../../notes/types'

const namespace = 'tags'
const { mapGetters, mapActions } = createNamespacedHelpers(namespace)

export default {
  data () {
    return {
    }
  },
  components: { Tag },
  methods: {
    ...mapActions(Object.keys(actions)),
    getNotesByTag (tag) {
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
