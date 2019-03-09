<template>
  <div>
    <v-layout row align-center class="flex-container">
      <search fluid class="flex-item"/>
      <new-professor v-on:validated="updateProfs" class="flex-item"/>
    </v-layout>
    <v-snackbar
      v-model="snackbar"
      :timeout="timeout"
      top
      left
    >
      Post Created Successfully
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
      show: false,
      snackbar: false,
      y: 'top',
      x: null,
      mode: '',
      timeout: 2000,
    }
  },

  methods: {
    updateProfs() {
      axios.get('http://localhost:8000/api/professors/')
          .then(res => {
              let prof = res.data[res.data.length - 1]
              console.log(prof)
              prof['first_last'] = prof.first_name + " " + prof.last_name
              this.professors.unshift(prof)
          })
          .then(this.snackbar = true)
          .catch(e => {
              console.error(e)
          })
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
