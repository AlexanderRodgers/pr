<template>
    <v-container>
        <v-layout>
            <v-flex xs3>
                <!-- <stats-card/> -->
                <gpa-card :gpa="3.5"/>
                <subheader/>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import StatsCard from '~/components/helper/StatsCard'
import GpaCard from '~/components/stats/Gpa'
import Subheader from '~/components/stats/Subheader'
export default {

    components: {
        StatsCard,
        GpaCard,
        Subheader,
    }

}
</script>

<style>

</style>
