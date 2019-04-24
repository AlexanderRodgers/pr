<template>
    <v-container fluid>
        <v-layout row align-center class="flex-container">
            <span class="flex-item"><h1>{{ data.first_name + " " + data.last_name }}</h1></span>
            <span class="flex-item" style="float:left;"><new-review :professor="data" v-on:review-valid="addReview"/></span>
            <prof-filter @selection="filterProfs"/>
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
import ProfFilter from '~/components/ProfFilter'

export default {

    components: {
        Review,
        NewReview,
        ProfileInfo,
        ProfFilter,
    },

    mixins: [gradeToGpa],

    data() {
        return {
            dev: 'http://localhost:8000/',
            gpa: 0,
            filterSelection: 0,
            inverseFilter: 1,
        }
    },

    methods: {
        addReview(newReview) {
            this.data.reviews.push(newReview)
        },

        filterProfs(filterId) {
            console.log(filterId)
            if (this.filterSelection !== filterId) {
                switch(filterId) {
                    case 1:
                        this.filterByRating()
                        break
                    case 2:
                        this.filterByDifficulty()
                        break
                    case 3:
                        this.filterByClass()
                        break
                    default:
                        console.log('error')
                }
            } 
        },

        filterByRating() {
            this.data.reviews.sort((a, b) => {
                return this.inverseFilter * (this.gradeToGpa[b.rating] - this.gradeToGpa[a.rating])
            })
        },

        filterByDifficulty() {
            this.data.reviews.sort((a, b) => {
                return this.inverseFilter * (a.difficulty - b.difficulty)
            })
        },

        filterByClass() {
            this.data.reviews.sort((a, b) => {
                return this.inverseFilter * (a.class_num - b.class_num)
            })
        }

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

.flex-item:nth-of-type(2) {
  flex-grow: 1 !important;
}

</style>
   