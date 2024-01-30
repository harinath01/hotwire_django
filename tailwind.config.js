/** @type {import('tailwindcss').Config} */
const Path = require("path");
const pwd = process.env.PWD;

// We can add current project paths here
const projectPaths = [
    Path.join(pwd, "./templates/**/*.html"),
    // add js file paths if you need
];


module.exports = {
  content: [...projectPaths],
  theme: {
    extend: {},
  },
  plugins: [],
}

