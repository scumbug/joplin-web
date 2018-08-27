import axios from 'axios'

export function fetchFolders () {
  return new Promise((resolve, reject) => {
    axios.get('http://127.0.0.1:8001/api/jw/folders/')
      .then((res) => { resolve(res.data.results) })
      .catch(error => { reject(error.statusText) })
  })
}

export function createFolder (folder) {
  return new Promise((resolve, reject) => {
    axios.post('http://127.0.0.1:8001/api/jw/folders/', folder)
      .then((res) => { resolve(res.data.results) })
      .catch(error => { reject(error.statusText) })
  })
}

export function updateFolder (folder) {
  return new Promise((resolve, reject) => {
    axios.patch('http://127.0.0.1:8001/api/jw/folders/' + folder.id + '/', folder)
      .then((res) => { resolve(res.data.results) })
      .catch(error => { reject(error.statusText) })
  })
}

export function deleteFolder (id) {
  return new Promise((resolve, reject) => {
    axios.delete('http://127.0.0.1:8001/api/jw/folders/' + id)
      .then((res) => { resolve(res.data.results) })
      .catch(error => { reject(error.statusText) })
  })
}

export default {
  fetchFolders,
  createFolder,
  updateFolder,
  deleteFolder
}
