<template>
  <v-app>
    <v-toolbar
      class="primary"
      fixed
      app
    >
      <nuxt-link to="/">
        <v-toolbar-title class="white--text">Poly<b>Ratings</b></v-toolbar-title>
      </nuxt-link>
    </v-toolbar>
    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
    <v-footer
      class="justify-center"
      app
    >
      <span>Made in Yosemite Tower 1 with Love <3</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      
    }
  }
}
</script>
