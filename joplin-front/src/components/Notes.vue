<template>
    <div class="col-3">
        <ul class="list-group">
        <note v-for="note in notes" :key="note.id">
            <li class="list-group-item"><a href="#" @click="editNote(note)">{{ note.title }}</a></li>
        </note>
        </ul>
      <div class="panel-footer">
          <button class="btn btn-success" @click="newNote()">Note</button>
      </div>
    </div>
</template>

<script>
// note content
import Note from './Note.vue'

import { mapActions } from 'vuex'

export default {
  data () {
    return {
      // notes: [],
      page: 1,
      q: ''
    }
  },
  components: { Note },
  methods: {
    ...mapActions([
      'loadNotes',
      'editNote',
      'removeNote'
    ]),
    editNote (note) {
      this.$store.dispatch('editNote', note)
    },
    delNote (id) {
      this.$store.dispatch('removeNote', id)
    },
    searchNote () {
    }
  },
  mounted () {
    this.q = ''
  },
  computed: {
    notes () {
      return this.$store.getters.notes
    }
  },
  created () {
    return this.$store.dispatch('loadNotes')
  }
}
</script>
