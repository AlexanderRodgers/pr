<template>
  <v-container fill-height>
      <v-layout row align-center class="flex-container">
        <search fluid class="flex-item"/>
        <new-professor class="flex-item"/>
      </v-layout>
  </v-container>
</template>

<script>
import profs from '~/mixins/profs.js'
import Search from '~/components/Search'
import NewProfessor from '~/components/NewProfessor'
export default {
  components: {
    Search,
    NewProfessor,
  },

  mixins: [profs],
}
</script>

<style scoped>
.flex-container {
  display: flex;
}

.flex-item:nth-of-type(1) {
  flex-grow: 2 !important;
}

</style>
