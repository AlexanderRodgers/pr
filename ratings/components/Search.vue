<template>
<v-container fluid fill-height>
	<v-layout align-center fill-height>
		<v-autocomplete
				:items="professors"
				placeholder="Search for a Professor"
				append-icon="search"
				item-text="first_last"
				item-value="id"
				:search-input.sync="search"
				:rules="[searchValid(search)]"
				@click:append="runSearch(search)"
				@keyup.enter="runSearch(search)"
				return-objects
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
			class="font-weight-light white--text avatar">N/A</v-list-tile-avatar>

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
export default {

	props: {
		professors: Array,
	},

    // mixins: [profs],

    data() {
        return { 
            search: '',
			dev: 'http://localhost:8000/',
        }
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
            let isProfessor = function(profs) {
                return search === profs.first_last
			}
			if(!search || search == null) {
				return true
			}
            return this.professors.some(isProfessor)
                ? true
                : "That professor doesn't exist"
		},
		
		professorBySearch(search) {
			for (let prof of this.professors) {
				if (prof.first_last === search) {
					return prof
				}
			}
			return null
		},

        runSearch(search) {
			console.log(search)
			let prof = this.professorBySearch(search)
            if(search && prof != null) {
                this.$router.push('/professors/' + prof.id)  
            }
            
		},
		
		getMajor(majorId) {
			axios.get(this.dev + 'api/majors/' + majorId)
				.then(res => {
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
