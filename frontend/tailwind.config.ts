import type { Config } from "tailwindcss";
import {addIconSelectors} from "@iconify/tailwind";
import tailwindCrossbar from 'tailwind-scrollbar'

export default <Partial<Config>>{
  content: [
    `./components/**/*.{vue,js,ts}`,
    `./layouts/**/*.vue`,
    `./pages/**/*.vue`,
    `./composables/**/*.{js,ts}`,
    `./plugins/**/*.{js,ts}`,
    `./utils/**/*.{js,ts}`,
    `./App.{js,ts,vue}`,
    `./app.{js,ts,vue}`,
    `./Error.{js,ts,vue}`,
    `./error.{js,ts,vue}`,
    `./app.config.{js,ts}`,
    "./node_modules/primevue/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {

  },

  darkMode: "class",
  plugins: [
    // require("tailwind-scrollbar"),
    tailwindCrossbar,
    // addDynamicIconSelectors()
    addIconSelectors([
      'mdi', 'mdi-light','eos-icons','arcticons',
    ]),
  ],
};