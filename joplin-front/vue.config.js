module.exports = {
  devServer: {
    proxy: {
        '/api/jw': {
            target: 'http://127.0.0.1:8001'
        }
    }
  }
}