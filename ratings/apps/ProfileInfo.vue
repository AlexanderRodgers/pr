<template>
    <v-container>
        <v-layout>
            <v-flex>
                {{ profile }}
                <!-- <info-card></info-card> -->
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import InfoCard from '~/components/stats/InfoCard'
export default {
    components: {
        InfoCard,
    },

    props: {
        profile: {
            Type: Object,
            required: true,
        }
    },

    data() {
        return {
            stats: {},
        }
    },

    methods: {
        setupGPA() {
            this.stats.header = 'GPA'
            let gpa = this.profile.gpa
            this.stats.mVal = gpa.toString()
            if(gpa > 3.0) {
                this.stats.bgColor = "green"
                this.stats.mSubheader = "Mostly positive"
            }
        }
    },

    mounted() {
        this.setupGPA()
    }
}
</script>

<style>

</style>
