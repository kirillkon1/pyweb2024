// postcss.config.js
module.exports = {
  plugins: [
    require('cssnano')({
      preset: 'default',
    }),
    // Добавьте другие плагины PostCSS при необходимости
  ],
};
