// src/plugins/vuetify.js

import Vue from 'vue'
import Vuetify from 'vuetify/lib'

Vue.use(Vuetify)

const vuetify = new Vuetify({
  theme: {
    themes: {
      light: {
            primary: "#1976D2",
            secondary: '#E1F5FE'
      },
    },
  },
})

export default vuetify
