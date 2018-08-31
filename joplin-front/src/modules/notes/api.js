import axios from 'axios'

export function fetchNotes () {
  return new Promise((resolve, reject) => {
    axios.get('http://127.0.0.1:8001/api/jw/notes/')
      .then((res) => { resolve(res.data.results) })
      .catch(error => { reject(error.statusText) })
  })
}

export function fetchNotesByFolder (folder) {
  return new Promise((resolve, reject) => {
    axios.get('http://127.0.0.1:8001/api/jw/notes/folder/' + folder)
      .then((res) => { resolve(res.data.results) })
      .catch(error => { reject(error.statusText) })
  })
}

export function fetchNotesByTag (tag) {
  return new Promise((resolve, reject) => {
    axios.get('http://127.0.0.1:8001/api/jw/notes/tag/' + tag)
      .then((res) => { resolve(res.data.results) })
      .catch(error => { reject(error.statusText) })
  })
}

export function createNote (note) {
  return new Promise((resolve, reject) => {
    axios.post('http://127.0.0.1:8001/api/jw/notes/', note)
      .then((res) => { resolve(res.data.results) })
      .catch(error => { reject(error.statusText) })
  })
}

export function updateNote (note) {
  return new Promise((resolve, reject) => {
    console.log(note)
    axios.patch('http://127.0.0.1:8001/api/jw/notes/' + note.id + '/', note)
      .then((res) => { resolve(res.data.results) })
      .catch(error => { reject(error.statusText) })
  })
}

export function deleteNote (id) {
  return new Promise((resolve, reject) => {
    axios.delete('http://127.0.0.1:8001/api/jw/notes/' + id)
      .then((res) => { resolve(res.data.results) })
      .catch(error => { reject(error.statusText) })
  })
}

export default {
  fetchNotes,
  createNote,
  updateNote,
  deleteNote,
  fetchNotesByFolder,
  fetchNotesByTag
}
