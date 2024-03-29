/** @type {import('tailwindcss').Config} */
const Path = require("path");
const pwd = process.env.PWD;

// We can add current project paths here
const pySitePackages = process.env.pySitePackages;

// We can add current project paths here
const projectPaths = [
    Path.join(pwd, "./templates/**/*.html"),
    // add js file paths if you need
];

// We can add 3-party python packages here
let pyPackagesPaths = []
if (pySitePackages){
    pyPackagesPaths = [
        Path.join(pySitePackages, "./crispy_tailwind/**/*.html"),
        Path.join(pySitePackages, "./crispy_tailwind/**/*.py"),
        Path.join(pySitePackages, "./crispy_tailwind/**/*.js"),
    ];
}

const contentPaths = [...projectPaths, ...pyPackagesPaths];


module.exports = {
  content: [...contentPaths],
  theme: {
    extend: {},
  },
  plugins: [require('@tailwindcss/forms')],
}

