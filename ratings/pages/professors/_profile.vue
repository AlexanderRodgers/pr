<template>
    <div>
        <h1>{{ data.first_name + " " + data.last_name }}</h1>
        <new-review :professor="data"/>
        <h3>{{ data }}</h3>

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
import NewReview from '~/components/NewReview'

export default {

    components: {
        Gpa,
        NumReviews,
        Review,
        NewReview,
    },

    data() {
        return {

        }
    },

    async asyncData({ params, error, payload }) {
        if (payload) return { data: payload }
        else return axios.get(`http://localhost:8000/api/professors/${params.profile}`)
        .then((res) => {
            return { data: res.data }
        })
        .catch(e => {
            throw new Error("Professor does not exist!");
            console.error(e)
        })
    },
}
</script>

<style>

</style>
   