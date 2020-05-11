module.exports = {
  "publicPath": "/",
  "outputDir": "dist",
  "assetsDir": "static",
  "lintOnSave": true,
  "productionSourceMap": false,
  "devServer": {
    "host": "localhost",
    "port": "8080",
    "hot": true,
    "open": true,
    "overlay": {
      "warning": true,
      "error": true
    }
  },
  "transpileDependencies": [
    "vuetify"
  ]
}