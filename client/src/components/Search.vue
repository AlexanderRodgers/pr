<template>
    <div>
        <v-autocomplete
            v-model="search"
            :items="professors"
            item-text="first_name"
            append-icon="search"
            @click:append="search"
        >

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
import axios from 'axios'
export default {
    data() {
        return {
            search: '',
            dev: 'http://localhost:8000',
            professors: [],
        }
    },

    methods: {
        runSearch() {
            console.log('Search function ran.')
        }
    },

    mounted() {
        axios.get(this.dev + '/api/reviews/')
            .then(res => {
                console.log(res)
                for (let prof of res.data) {
                    this.professors.push(prof)
                }
            })
    }
}
</script>

<style>

</style>
