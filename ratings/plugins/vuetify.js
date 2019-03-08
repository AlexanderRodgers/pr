import Vue from 'vue'
import Vuetify from 'vuetify/lib'
import colors from 'vuetify/es5/util/colors'

Vue.use(Vuetify, {
  theme: {
    primary: '#035642',
    secondary: '#EAAB00',
    positive: '#2E7D32', //'green darken-3'
    warning: '#FFEA00', // 'yellow accent-3'
    bad: '#B71C1C', // red darken-4
    neutral: '#546E7A', //blue-gray darken-1
  },
})

// theme: {
//   primary: '#121212', // a color that is not in the material colors palette
//   accent: colors.grey.darken3,
//   secondary: colors.amber.darken3,
//   info: colors.teal.lighten1,
//   warning: colors.amber.base,
//   error: colors.deepOrange.accent4,
//   success: colors.green.accent3
// }