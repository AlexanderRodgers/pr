<template>
  <v-app>
    <v-toolbar app class="primary">
      <v-toolbar-title class="headline text-uppercase">
        <span>Poly</span>
        <span class="font-weight-light">Ratings</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        flat
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
      >
        <span class="mr-2">Latest Release</span>
      </v-btn>
    </v-toolbar>

    <v-content>
      <Search/>
      <!-- <new-review/> -->
      <new-professor/>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import Search from './components/Search'
import NewReview from './components/NewReview'
import NewProfessor from './components/NewProfessor'

export default {
  name: 'App',
  components: {
    Search,
    NewReview,
    NewProfessor,
  },
  data () {
    return {
      //
    }
  }
}
</script>
