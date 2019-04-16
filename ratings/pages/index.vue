<template>
  <div>
    <v-layout row align-center class="flex-container">
      <search :professors="professors" fluid class="flex-item"/>
      <new-professor v-on:validated="updateProfs" class="flex-item"/>
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
import ProfessorApi from '~/services/api/professors.js'
import MajorApi from '~/services/api/majors.js'
import axios from 'axios'
export default {

  // mixins: [profs],

  components: {
    Search,
    NewProfessor,
  },

  data() {
    return {
      professors: [],
      majors: [],
      newPost: {},
      updateList: false,
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
      // Most likely need to make professors some sort of computed property to show changes. I can't figure it out at this moment.
      if (Object.entries(newProf).length === 0 && newProf.constructor === Object) {
        this.snackbarResponse = 'Unable to add professor'
      } else {
        MajorApi.getMajor(newProf['major'])
        .then(res => {
          newProf['major_stats'] = res
        })
        newProf['first_last'] = newProf.first_name + " " + newProf.last_name
        newProf['gpa'] = -1
        this.professors.push(newProf)
        this.snackbarResponse = `Professor ${newProf.last_name} added`
      }
      this.snackbar = true
    }
  },

  mounted() {
    MajorApi.getMajors()
      .then(res => {
        this.majors = res
      })
		let preCompProfessors = []
		ProfessorApi.getCompiledProfs()
			.then(res => {
				for (let prof of res) {
					if (prof.major != null) {
            prof['major_stats'] = this.majors.find(major => major.id === prof.id)
					}
					preCompProfessors.push(prof)
				}
			})
			.catch(e => console.log(e))
		console.log(preCompProfessors)
		this.professors = preCompProfessors
	},
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
