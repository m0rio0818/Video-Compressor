/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./dist/electron/**/*.{html,js,ts}'],
  theme: {
    extend: {},
  },
  plugins: [
    // require('tailwindcss-hover-plugin'),
  ],
}

