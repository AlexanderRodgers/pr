<template>
    <div>
    <v-text-field
            v-model="search"
            label="Search Your Professor"
            append-icon="search"
            @click:append="runSearch"
            outline
        ></v-text-field>
        </div>
</template>

<script>
export default {
    data() {
        return {
            search: '',
        }
    },

    methods: {
        runSearch() {
            console.log('Search function ran.')
        }
    }
}
</script>

<style>

</style>
