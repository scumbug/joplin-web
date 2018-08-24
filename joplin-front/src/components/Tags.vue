<template>
    <div class="col">
        <nav class="panel">
            <p class="panel-heading">
                <span class="panel-icon"></span> Tags
            </p>
            <tag v-for="tag in tags" :key="tags.id">{{ tag.tag }}</tag>
        </nav>
    </div>
</template>

<script>
import Tag from './Tag.vue'

export default {
  data () {
    return {
      tags: []
    }
  },
  components: { Tag },
  mounted () {
    this.axios.get('http://127.0.0.1:8001/api/jw/tags/')
      .then(response => {
        this.tags = response.data
      }).catch(error => {
        console.log(error)
      })
  }
}
</script>