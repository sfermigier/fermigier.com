// const { colors } = require("tailwindcss/defaultTheme");
const colors = require("tailwindcss/colors");

module.exports = {
  content: [
    /**
     * HTML. Paths to template files that will contain Tailwind CSS classes.
     */
    "./**/templates/**/*.html",
    "./**/*.j2",
  ],
  theme: {
    extend: {
      colors: {
        brand: colors.blue,

        // Not used
        // a17t colors
        // neutral: colors.slate,
        // positive: colors.green,
        // urgent: colors.violet,
        // warning: colors.yellow,
        // info: colors.blue,
        // critical: colors.red,
        // // flowbite colors
        // primary: colors.blue,
      },
      spacing: {
        "80": "20rem",
        "108": "27rem",
      },
      borderWidth: {
        "14": "14px",
      },
    },
    container: {
      padding: "1rem",
    },

    fontFamily: {
      sans: [
        "Nunito Sans",
        "Roboto",
        "-apple-system",
        "BlinkMacSystemFont",
        '"Segoe UI"',
        '"Helvetica Neue"',
        "Arial",
        '"Noto Sans"',
        "sans-serif",
        '"Apple Color Emoji"',
        '"Segoe UI Emoji"',
        '"Segoe UI Symbol"',
        '"Noto Color Emoji"',
      ],
      serif: ["Georgia", "Cambria", '"Times New Roman"', "Times", "serif"],
      mono: [
        "Menlo",
        "Monaco",
        "Consolas",
        '"Liberation Mono"',
        '"Courier New"',
        "monospace",
      ],
    },
  },
  variants: {
    // Some useful comment
  },
  plugins: [
    // Some useful comment
  ],
};
