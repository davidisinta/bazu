// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    "nuxt-primevue",
    "@pinia/nuxt",
    "@nuxtjs/tailwindcss",
    "@vueuse/nuxt",
    "nuxt-icon",
    "nuxt-ark-ui",
    "nuxt-primevue",
    "@nuxt/image",
    "@hebilicious/vue-query-nuxt",
    "@nuxtjs/supabase",
  ],
  devServer: {
    port: 3002,
  },
  ssr: false, //since this is frontend only
  router: {
    options: {
      scrollBehaviorType: "smooth",
    },
  },
  app: {
    head: {
      titleTemplate: "%s | Bazu",
      meta: [
        { charset: "utf-8" },
        { name: "viewport", content: "width=device-width, initial-scale=1" },
        { name: "description", content: "Meta description" },
      ],
    },
  },

  primevue: {
    cssLayerOrder: "tailwind-base,primevue,tailwind-utilities",
    usePrimeVue: true,
    components: {
      prefix: "Prime",
      include: [
        "Menubar",
        "Dropdown",
        "Avatar",
        "ProgressSpinner",
        "Listbox",
        "Splitter",
        "SplitterPanel",
        "Rating",
        "Card",
      ],
    },
    importPT: { as: "Tailwind", from: "~/primevue-tailwind-pt.ts" },

    options: {
      unstyled: false,
      ripple: true,
    },
  },
  tailwindcss: {
    cssPath: "~/assets/css/tailwind.css",
    editorSupport: true,
  },

  typescript: {
    typeCheck: true,
    strict: true,
    shim: false,
  },

  pinia: {
    /* autoImports: ["defineStore", "skipHydrate", "storeToRefs"], */
    // storesDirs:['./stores*','./stores']
  },
  supabase: {
    redirect: false,
    redirectOptions: {
      login: "/login",
      callback: "/confirm",
      exclude: ["/signup"],
    },
  },

  "ark-ui": {
    prefix: "Ark",
  },
  imports: {
    autoImport: true,
    dirs: [
      "composables/*.{ts,js,mjs,mts}",
      "composables/*.{ts,js,mjs,mts}",
      "types",
      "stores",
    ],
  },
});