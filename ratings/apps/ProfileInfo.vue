<template>
    <v-container>
        <v-layout>
            <v-flex xs3>
                <info-card :stats="stats"></info-card>
            </v-flex>
            <v-flex>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import InfoCard from '~/components/stats/InfoCard'
import gradeToGpa from '~/mixins/gradeToGpa.js'
export default {

    mixins: [gradeToGpa],

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
            this.stats.mHeader = 'GPA'
            let gpa = this.profile.gpa
            this.stats.mVal = gpa.toString()
            if(gpa > 3.0) {
                this.stats.bgColor = "green"
                this.stats.mSubheader = "Mostly positive"
            } else if (gpa > 2.0) {
                this.stats.bgColor = "yellow"
                this.stats.mSubheader = "Mixed ratings"
            } else {
                this.stats.bgColor = "red"
                this.stats.mSubheader = "Mostly negative"
            }
        },

        aggregateReviews() {
            let reviews = this.profile.reviews
            if (reviews.length < 3) {
                this.stats.subheading = 'Trend Not available'
                this.stats.subheadingImage = 'trending_flat'
            } else {
                // Need to refactor when I take stats lmao
                let lastReviews = reviews.slice(Math.max(reviews.length - 3), 0)
                let lastValue = this.convertToGpa(lastReviews[0].rating)
                let down = false 
                for (let r of lastReviews) {
                    if (this.convertToGpa(r.rating) <= lastValue) {
                        lastValue = r.rating
                    } else {
                        down = true
                        this.stats.subheading = 'Trending Downwards'
                        this.stats.subheadingImage = 'trending_down'
                    }
                }
                if(!down) {
                    this.stats.subheading = 'Trending Upwards'
                    this.stats.subheadingImage = 'trending_up'
                }

            }
        }
    },

    mounted() {
        this.setupGPA()
        this.aggregateReviews()
    }
}
</script>

<style>

</style>
