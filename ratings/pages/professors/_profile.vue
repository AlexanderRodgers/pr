<template>
    <div>
        <h1>{{data.first_name + " " + data.last_name}}</h1>
        <h3>{{data}}</h3>
        <!-- <v-layout justify-center column>
            <gpa :gpa="data.gpa"/>
            <num-reviews :numReviews="data.reviews.length"/>
        </v-layout> -->
        <review 
            v-for="(review, ind) in data.reviews"
            :key="review.id" :review="data.reviews[ind]"/>
    </div>
</template>

<script>
import axios from 'axios'
import Gpa from '~/components/stats/Gpa'
import NumReviews from '~/components/stats/NumReviews'
import Review from '~/components/Review'

export default {

    components: {
        Gpa,
        NumReviews,
        Review
    },

    data() {
        return {

        }
    },

    async asyncData({ params }) {
    // return {data: params}
    return axios.get(`http://localhost:8000/api/professors/${params.profile}`)
        .then((res) => {
            return { data: res.data }
        })
    },
}
</script>

<style>

</style>
   