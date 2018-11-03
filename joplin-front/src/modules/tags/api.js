import axios from 'axios'

export function fetchTags () {
  return new Promise((resolve, reject) => {
    axios.get('/api/jw/tags/')
      .then((res) => { resolve(res.data) })
      .catch(error => { reject(error.statusText) })
  })
}

export function createTag (tag) {
  return new Promise((resolve, reject) => {
    axios.post('/api/jw/tags/', tag)
      .then((res) => { resolve(res.data) })
      .catch(error => { reject(error.statusText) })
  })
}

export function updateTag (tag) {
  return new Promise((resolve, reject) => {
    axios.patch('/api/jw/tags/' + tag.id + '/', tag)
      .then((res) => { resolve(res.data) })
      .catch(error => { reject(error.statusText) })
  })
}

export function deleteTag (id) {
  return new Promise((resolve, reject) => {
    axios.delete('/api/jw/tags/' + id)
      .then((res) => { resolve(res.data) })
      .catch(error => { reject(error.statusText) })
  })
}

export default {
  fetchTags,
  createTag,
  updateTag,
  deleteTag
}
