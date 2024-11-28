/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        title: "#343A40",
        description: "#6C757D",
        price: "#28A745",
        primary: "#F8F9FA",
      }
    },
  },
  plugins: [],
}
