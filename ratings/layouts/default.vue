<template>
  <v-app>
    <v-toolbar
      class="primary"
      :clipped-left="clipped"
      fixed
      app
    >
      <v-toolbar-title>Poly<b>Ratings</b></v-toolbar-title>
    </v-toolbar>
    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
    <v-footer
      :fixed="fixed"
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
