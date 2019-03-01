<template>
    <div>
        <v-autocomplete
            v-model="search"
            :items="professors"
            placeholder="Search for a Professor"
            append-icon="search"
            item-text="first_last"
            item-value="id"
            @click:append="search"
        >

        <template
        slot="item"
        slot-scope="{ item, tile }"
      >
      <a :href="'/professors/'+toSlug(item.first_last)"></a>
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
        runSearch() {
            console.log('Search function ran.')
        },

        toSlug(urlString) {
            return slugify(urlString, {
                lower: true
            })
        }
    },
}
</script>

<style>

</style>
