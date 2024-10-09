module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  darkMode: 'class', // This enables the dark mode variant
  theme: {
    extend: {
      colors: {
        'space-dark': '#0f0c29',
        'space-mid': '#302b63',
        'space-light': '#24243e',
        'star-white': '#ffffff',
        'purple-light': '#D6BCFA'
      },
    },
  },
  plugins: [],
}