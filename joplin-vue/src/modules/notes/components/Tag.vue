<template>
  <span>
    <span v-for="tag in parent_folder" :key="tag.id">
      <b-badge pill variant="success" >{{ tag.title }}</b-badge>&nbsp;
    </span>
  </span>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'

import getters from '../getters'

const namespace = 'tags'
const { mapGetters } = createNamespacedHelpers(namespace)

export default {
  name: 'Tag',
  props: {
    parent_folder: Object
  },
  computed: {
    ...mapGetters(Object.keys(getters))
  }
}

</script>
