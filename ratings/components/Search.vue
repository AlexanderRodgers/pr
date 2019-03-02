<template>
    <div>
        <!-- The autocomplete component is giving me weird effects when a user tries deleting their search. -->
        <v-autocomplete
            v-model="search"
            :items="professors"
            placeholder="Search for a Professor"
            append-icon="search"
            item-text="first_last"
            item-value="id"
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
          color="indigo"
          class="headline font-weight-light white--text"
        >
          {{ item.first_name.charAt(0) }}
        </v-list-tile-avatar>
        <v-list-tile-content>
          <v-list-tile-title v-text="item.first_last"></v-list-tile-title>
          <v-list-tile-sub-title v-text="item.major"></v-list-tile-sub-title>
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
    </div>
</template>

<script>
import slugify from 'slugify'
import profs from '~/mixins/profs.js'
export default {

    mixins: [profs],

    data() {
        return {
            search: '',
            dev: 'http://localhost:8000',
            professors: [],
        }
    },

    methods: {

        searchValid(search) {
            var isProfessor = function(profs) {
                return search === profs.id
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
    },
}
</script>

<style>

</style>
