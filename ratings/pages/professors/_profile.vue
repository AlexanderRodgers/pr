<template>
<div>
    <!-- <gpa :gpa="gpa"/> -->
    <div>
        <h1>{{ data.first_name + " " + data.last_name }}</h1>
        <new-review :professor="data" v-on:review-valid="addReview"/>
        <review 
            v-for="(review, ind) in data.reviews"
            :key="review.id" :review="data.reviews[ind]"/>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import Gpa from '~/components/stats/Gpa'
import Review from '~/components/Review'
import NewReview from '~/components/NewReview'
import gradeToGpa from '~/mixins/gradeToGpa.js'

export default {

    components: {
        Gpa,
        Review,
        NewReview,
    },

    mixins: [gradeToGpa],

    data() {
        return {
            dev: 'http://localhost:8000/',
            gpa: 0,
        }
    },

    methods: {
        addReview(newReview) {
            this.data.reviews.push(newReview)
        },
    },

    async asyncData({ params, error, payload }) {
        if (payload) return { data: payload }
        else return axios.get(`http://localhost:8000/api/professors/${params.profile}`)
        .then(res => {
            return { data: res.data }
        })
        .catch(e => {
            console.error(e)
        })
    },

    mounted() {
        let gpa = 0
        this.data.reviews.sort((a, b) => {
            return a.class_num - b.class_num
        })
        for(let review of this.data.reviews) {
            gpa += this.gradeToGpa[review.rating]
        }
        this.gpa = parseFloat((gpa / this.data.reviews.length).toFixed(2))
    }

    
}
</script>

<style>

</style>
   