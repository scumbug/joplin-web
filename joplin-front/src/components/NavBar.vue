<template>
  <div>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Joplin Web</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
        </li>
      </ul>
      <form class="form-inline my-2 my-lg-0">
        <input class="form-control  mr-sm-2" type="search" v-model="q" @keyup.enter="searchNote()" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </form>
    </div>
  </nav>
  </div>
</template>

<script>
export default {
  props: ['bookName'],
  data () {
    return {
      q: ''
    }
  },
  methods: {
    searchNote () {
      this.$store.emit('searchNote', this.q)
    }
  }
}
</script>
