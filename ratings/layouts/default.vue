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
      app
    >
      <span class="text-lg-center">Made in Yosemite with Love <3</span>
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
