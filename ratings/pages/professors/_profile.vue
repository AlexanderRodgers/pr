<template>
    <v-container fluid>
        <v-layout row align-center class="flex-container">
            <span class="flex-item"><h1>{{ data.first_name + " " + data.last_name }}</h1></span>
            <span class="flex-item"><new-review :professor="data" v-on:review-valid="addReview"/></span>
        </v-layout>
        <!-- <v-layout>
            <v-flex>
                <profile-info :profile="data"></profile-info>
            </v-flex>
        </v-layout> -->
        <v-layout>
            <v-flex>
                <review 
                    v-for="(review, ind) in data.reviews"
                    :key="review.id" :review="data.reviews[ind]"/>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import axios from 'axios'
import Review from '~/components/Review'
import NewReview from '~/components/NewReview'
import gradeToGpa from '~/mixins/gradeToGpa.js'
import ProfileInfo from '~/apps/ProfileInfo'

export default {

    components: {
        Review,
        NewReview,
        ProfileInfo
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
            error({statusCode: 404, message: 'Professor not found.'})
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

<style scoped>
.flex-container {
  display: flex;
}

.flex-item:nth-of-type(1) {
  flex-grow: 2 !important;
}

</style>
   