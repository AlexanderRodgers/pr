<template>
<v-container fluid fill-height>
	<v-layout align-center fill-height>
		<!-- The autocomplete component is giving me weird effects when a user tries deleting their search. -->
		<v-autocomplete
				:items="professors"
				placeholder="Search for a Professor"
				append-icon="search"
				item-text="first_last"
				item-value="id"
				cache-items
				:search-input.sync="search"
				:rules="[searchValid(search)]"
				@click:append="runSearch(search)"
				@keyup.enter="runSearch(search)"
		>

		<template
		slot="item"
		slot-scope="{ item }"
	>
	<a :href="'/professors/'+item.id"></a>
		<v-list-tile-avatar
			v-if="item.gpa !== -1"
			:color=colorIcon(item)
			class="font-weight-light white--text avatar"
		>
			{{ item.gpa.toFixed(1) }}
		</v-list-tile-avatar>

		<v-list-tile-avatar
			v-else
			color="blue-grey darken-1"
			class="font-weight-light white--text avatar"
		>
			N/A
		</v-list-tile-avatar>

		<v-list-tile-content>
			<v-list-tile-title v-text="item.first_last"></v-list-tile-title>
			<v-list-tile-sub-title >{{ item.major_stats ? item.major_stats.major : '' }}</v-list-tile-sub-title>
		</v-list-tile-content>
		<v-list-tile-action>
			<v-icon>face</v-icon>
		</v-list-tile-action>
	</template>

		</v-autocomplete>

		<template slot="no-data">
				<v-list-tile>
						<v-list-tile-title>
								Search for a Professor
						</v-list-tile-title>
				</v-list-tile>
		</template>
	</v-layout>
</v-container>
</template>

<script>
import axios from 'axios'
import slugify from 'slugify'
import profs from '~/mixins/profs.js'
import ProfessorApi from '~/services/api/professors.js'
import MajorApi from '~/services/api/majors.js'
export default {

    // mixins: [profs],

    data() {
        return {
			professors: [], 
			myProfs: [],
            search: '',
            dev: 'http://localhost:8000',
        }
	},
	
	mounted() {
		let preCompProfessors = []
		ProfessorApi.getCompiledProfs()
			.then(res => {
				for (let prof of res) {
					if (prof.major != null) {
						MajorApi.getMajor(prof['major'])
							.then(res => {
								prof['major_stats'] = res
							})
					}
					preCompProfessors.push(prof)
				}
			})
			.catch(e => console.log(e))
		console.log(preCompProfessors)
		this.professors = preCompProfessors
	},

    methods: {
        colorIcon(profObj) {
            if(profObj.gpa === -1) {
							return "neutral"
						}
						else if(profObj.gpa > 3.0) {
							return "positive"
						}
						else if(profObj.gpa > 2.0) {
							return "warning"
						}
						else {
							return "bad"
						}
        },

        searchValid(search) {
            var isProfessor = function(profs) {
                return search === profs.id
			}
			if(!search || search == null) {
				return true
			}
            return this.professors.some(isProfessor)
                ? true
                : "That professor doesn't exist"
        },

        runSearch(search) {
            if(search) {
                this.$router.push('/professors/' + search)  
            }
            
		},
		
		getMajor(majorId) {
			axios.get('http://localhost:8000/api/majors/' + majorId)
				.then(res => {
					console.log(res.data.major)
					return res.data.major
				})
				.catch(e => {
					console.log(e)
				})
			
		}
	},
}
</script>

<style scoped>

</style>
