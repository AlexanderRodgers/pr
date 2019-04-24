<template>
    <v-form ref="form">
        <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
        <v-btn 
            slot="activator"
            color="primary"
            dark
            small
            fab>
                <v-icon>add</v-icon>
        </v-btn>
            <v-card>
                <v-toolbar dark color="primary">
                    <v-btn icon dark @click="dialog = false">
                        <v-icon>close</v-icon>
                    </v-btn>
                    <v-toolbar-title>Rate {{ professor.first_name + ' ' + professor.last_name }}</v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-toolbar-items>
                        <v-btn dark flat @click="persist">Save</v-btn>
                    </v-toolbar-items>
                </v-toolbar>
            <v-container>
                <h2>{{ professor.first_name + ' ' + professor.last_name }}'s Rating</h2>
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
                    </v-flex>
                    <v-flex xs12 sm6 md3 >
                        <v-select
                            :items="major"
                            item-text="abbreviation"
                            item-value="id"
                            v-model="postData.major"
                            label="Major"
                            :rules="[v => !!v || 'This field is required']"
                            required
                        />
                    </v-flex>
                        <v-radio-group 
                        mandatory
                        :rules="[v => v == 0 || !!v || 'This field is required']"
                        v-model="postData.quarter">
                        <v-radio
                        v-for="(item, index) in quarterLabel"
                        :key="index"
                        :label="item"
                        :value="index"
                        />
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
        professor: Object,
    },

    data() {
        return {
            dev: 'http://localhost:8000/api/',
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
                this.submit()
            }
        },

        submit() {
            this.postData['professor'] = this.professor.id
            console.log(this.postData)
            axios.post(this.dev + `reviews/${this.professor.id}/`, this.postData)
                .then(res => {
                    if(res.status === 201) {
                        this.$emit('review-valid', this.postData)
                    } else if (res.status === 404) {
                        console.log('404: professor not found.')
                    }
                    this.dialog = false;
                })
                .catch(e => console.error(e))
        },

        persist() {
            // Creating a deep copy so we don't modify the postData
            let persistedInfo = JSON.parse(JSON.stringify(this.postData))
            persistedInfo['id'] = this.professor.id
            localStorage.formData = JSON.stringify(persistedInfo)
            this.dialog = false
        }
    },

    mounted() {
        axios.get(this.dev + 'majors/')
            .then(res => {
                for (let major of res.data) {
                    this.major.push(major)
                }
            })
        if (localStorage.formData) {
            let parsedStorage = JSON.parse(localStorage.formData)
            if (parsedStorage.id === this.professor.id) {
                this.postData = parsedStorage
            }
        }
    }
}
</script>

<style>

</style>
