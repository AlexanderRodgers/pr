<template>
    <v-form ref="form">
        <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
        <v-btn slot="activator" color="primary" dark>New Review</v-btn>
            <v-card>
                <v-toolbar dark color="primary">
                    <v-btn icon dark @click="dialog = false">
                        <v-icon>close</v-icon>
                    </v-btn>
                    <v-toolbar-title>Rate {{ professor }}</v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-toolbar-items>
                        <v-btn dark flat @click="dialog = false">Save</v-btn>
                    </v-toolbar-items>
                </v-toolbar>
            <v-container>
                <h2>{{ professor }}'s Rating</h2>
                <v-select
                    :items="rating"
                    v-model="postData.rating"
                    label="Professor Rating"
                    :rules="[v => !!v || 'This field is required']"
                    required
                />
                <h3>How difficult was the course?</h3>
                <v-select
                    :items="difficulty"
                    v-model="postData.difficulty"
                    label="Difficulty"
                    :rules="[v => !!v || 'This field is required']"
                    required
                />
                <h3>What grade did you get in the class?</h3>
                <v-select
                    :items="classGrade"
                    v-model="postData.class_grade"
                    label="Class Grade"
                    :rules="[v => !!v || 'This field is required']"
                    required
                />
                <v-layout>
                    <v-flex xs12 sm4 md2>
                        <v-text-field
                            v-model="postData.class_num"
                            label="Class Number"
                            :rules="[v => !!v || 'This field is required', v => v > 99 && v < 700 || 'Class number is invalid']"
                            mask="###"
                            required
                        />
                        <!-- <v-text-field
                            label="Year Taken"
                            v-model="yearTaken"
                            mask="####"
                            :rules="[formRules.validateYear(yearTaken)]"/> -->
                    </v-flex>
                    <v-flex xs12 sm6 md3 >
                        <v-select
                            :items="major"
                            item-text="abbreviation"
                            label="Major"
                            :rules="[v => !!v || 'This field is required']"
                            required
                        />
                    </v-flex>
                        <v-radio-group 
                    v-model="quarter">
                        <v-radio
                        v-for="(item, index) in quarterLabel"
                        :key="index"
                        :label="item"
                        :value="index"/>
                    </v-radio-group>
                </v-layout>
                <v-textarea
                    v-model="postData.review"
                    auto-grow
                    label="Review"
                    placeholder="John Smith is a wonderful teacher!"
                    counter="10000"
                    :rules="[v => !!v || 'This field is required']"
                    required
                    />
                <v-spacer></v-spacer>
                <v-btn color="primary" @click="validate">Submit</v-btn>
            </v-container>
            
            </v-card>
        </v-dialog>
    </v-form>
</template>

<script>
import axios from 'axios'
import reviewConstants from '~/mixins/reviewConstants.js'
export default {

    mixins: [reviewConstants],

    props: {
        professor: String,
    },

    data() {
        return {
            dialog: false,
            postData: {},
            classNum: 0,
            quarter: 0,
            quarterLabel: ['Fall', 'Winter', 'Spring', 'Summer'],
            major: [],
            yearTaken: '',
            review: '',
        }
    },

    methods: {
        validate() {
            if (this.$refs.form.validate()) {
                console.log('Review valid')
                this.submit()
            }
        },

        submit() {
            //TODO: The entire method. Also fill in the v-model values for the rest of the form.
        }
    },

    mounted() {
        axios.get('http://localhost:8000/api/majors/')
            .then(res => {
                for (let major of res.data) {
                    this.major.push(major)
                }
            })
    }
}
</script>

<style>

</style>
