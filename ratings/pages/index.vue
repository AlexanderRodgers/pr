<template>
  <div>
    <v-layout row align-center class="flex-container">
      <search fluid class="flex-item"/>
      <new-professor v-on:validated="updateProfs($event)" class="flex-item"/>
    </v-layout>
    <v-snackbar
      v-model="snackbar"
      :timeout="timeout"
      top
      left
    >
      {{ snackbarResponse }}
      <v-btn
        color="pink"
        flat
        @click="snackbar = false"
      >
        Close
      </v-btn>
    </v-snackbar>
  </div>
</template>

<script>
import profs from '~/mixins/profs.js'
import Search from '~/components/Search'
import NewProfessor from '~/components/NewProfessor'
import axios from 'axios'
export default {

  mixins: [profs],

  components: {
    Search,
    NewProfessor,
  },

  data() {
    return {
      newPost: {},
      snackbarResponse: '',
      show: false,
      snackbar: false,
      y: 'top',
      x: null,
      mode: '',
      timeout: 2000,
    }
  },

  methods: {
    updateProfs(newProf) {
      // Check if object is empty.
      if (Object.entries(newProf).length === 0 && newProf.constructor === Object) {
        this.snackbarResponse = 'Unable to add professor'
      } else {
        newProf['first_last'] = newProf.first_name + " " + newProf.last_name
        this.professors.unshift(newProf)
        this.snackbarResponse = `Professor ${newProf.last_name} added`
      }
      this.snackbar = true
    }
  }
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
