import axios from 'axios'

export function fetchTags () {
  return new Promise((resolve, reject) => {
    axios.get('http://127.0.0.1:8001/api/jw/tags/')
      .then((res) => { resolve(res.data.results) })
      .catch(error => { reject(error.statusText) })
  })
}

export function createTag (tag) {
  return new Promise((resolve, reject) => {
    axios.post('http://127.0.0.1:8001/api/jw/tags/', tag)
      .then((res) => { resolve(res.data.results) })
      .catch(error => { reject(error.statusText) })
  })
}

export function updateTag (tag) {
  return new Promise((resolve, reject) => {
    axios.patch('http://127.0.0.1:8001/api/jw/tags/' + tag.id + '/', tag)
      .then((res) => { resolve(res.data.results) })
      .catch(error => { reject(error.statusText) })
  })
}

export function deleteTag (id) {
  return new Promise((resolve, reject) => {
    axios.delete('http://127.0.0.1:8001/api/jw/tags/' + id)
      .then((res) => { resolve(res.data.results) })
      .catch(error => { reject(error.statusText) })
  })
}

export default {
  fetchTags,
  createTag,
  updateTag,
  deleteTag
}
