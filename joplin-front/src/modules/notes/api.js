import axios from 'axios'

export function fetchNotes () {
  return new Promise((resolve, reject) => {
    axios.get('/api/jw/notes/')
      .then((res) => { resolve(res.data.results) })
      .catch(error => { reject(error.statusText) })
  })
}

export function fetchNotesByFolder (folder) {
  return new Promise((resolve, reject) => {
    axios.get('/api/jw/notes/folder/' + folder)
      .then((res) => { resolve(res.data.results) })
      .catch(error => { reject(error.statusText) })
  })
}

export function fetchNotesByTag (tag) {
  return new Promise((resolve, reject) => {
    axios.get('/api/jw/notes/tag/' + tag)
      .then((res) => { resolve(res.data.results) })
      .catch(error => { reject(error.statusText) })
  })
}

export function createNote (note) {
  return new Promise((resolve, reject) => {
    axios.post('/api/jw/notes/', note)
      .then((res) => { resolve(res.data) })
      .catch(error => { reject(error.statusText) })
  })
}

export function updateNote (note) {
  return new Promise((resolve, reject) => {
    axios.patch('/api/jw/notes/' + note.id + '/', note)
      .then((res) => { resolve(res.data) })
      .catch(error => { reject(error.statusText) })
  })
}

export function deleteNote (id) {
  return new Promise((resolve, reject) => {
    axios.delete('/api/jw/notes/' + id + '/')
      .then((res) => { resolve(res.data) })
      .catch(error => { reject(error.statusText) })
  })
}

export function fetchNoteTags (note) {
  return new Promise((resolve, reject) => {
    // this will trigger a retrieval of the tags of this note
    axios.get('/api/jw/notetags/' + note.id)
      .then((res) => {
        let tagString = ''
        for (let line in res.data.results) {
          let tag = res.data.results[line]['tag']
          tagString += tag.title + ', '
        }
        resolve(tagString)
      })
      .catch(error => { reject(error.statusText) })
  })
}

export default {
  fetchNotes,
  createNote,
  updateNote,
  deleteNote,
  fetchNotesByFolder,
  fetchNotesByTag,
  fetchNoteTags
}
