module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/static/'
    : '/',
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
