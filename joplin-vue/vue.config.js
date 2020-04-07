module.exports = {
  publicPath: process.env.NODE_ENV !== 'production'
    ? '/'
    : 'http://0.0.0.0:8001' + process.env.JW_BASE_URL + 'static',
  outputDir: '../joplin_web/static',
  indexPath: '../templates/index.html',
  filenameHashing: false,
  devServer: {
    proxy: {
        '/api/jw': {
            target: 'http://0.0.0.0:8001'
        }
    }
  }
}
