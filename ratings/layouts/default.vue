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
      <span>Alex Rodgers &copy; 2019</span>
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
