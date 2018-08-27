<template>
    <div class="col-2">
        <h3>Tags</h3>
        <div class="articles">
            <ul class="list-group">
                <tag v-for="tag in this.getTags" :key="tag.id">
                    <li class="list-group-item">
                        <a href="#" @click="notesByTag(tag.id)">{{ tag.title }}</a>
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

const namespace = 'tags'
const { mapGetters, mapActions } = createNamespacedHelpers(namespace)

export default {
  data () {
    return {
      page: 1,
      loading: true
    }
  },
  components: {Tag},
  methods: {
    ...mapActions(Object.keys(actions))
  },
  computed: {
    ...mapGetters(Object.keys(getters))
  },
  created () {
    this.$store.dispatch('tags/' + types.TAG_FETCH_ALL)
      .then(() => (this.loading = false))
  }
}
</script>
