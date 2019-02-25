<template>
    <v-form>
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
                    label="Professor Rating"
                    required
                />
                <h3>How difficult was the course?</h3>
                <v-select
                    :items="difficulty"
                    label="Difficulty"
                    required
                />
                <h3>What grade did you get in the class?</h3>
                <v-select
                    :items="classGrade"
                    label="Class Grade"
                    required
                />
                <v-layout>
                    <v-flex xs12 sm4 md2>
                        <v-text-field
                            v-model="classNum"
                            label="Class Number"
                            :rules="[formRules.validateClass(classNum)]"
                            mask="###"
                            required
                        />
                        <v-text-field
                            label="Year Taken"
                            v-model="yearTaken"
                            mask="####"
                            :rules="[formRules.validateYear(yearTaken)]"/>
                    </v-flex>
                    <v-flex xs12 sm6 md3 >
                        <v-select
                            :items="major"
                            item-text="abbreviation"
                            label="Major"
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
                    v-model="review"
                    auto-grow
                    label="Review"
                    placeholder="John Smith is a wonderful teacher!"
                    counter="10000"/>
                <v-spacer></v-spacer>
                <v-btn color="primary">Submit</v-btn>
            </v-container>
            
            </v-card>
        </v-dialog>
    </v-form>
</template>

<script>
import axios from 'axios'
export default {
    props: {
        professor: String,
    },

    data() {
        return {
            dialog: false,
            rating: ['A+', 'A', 'A-', 'B+', 'B', 'B-',
                    'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'],
            classGrade: ['A+', 'A', 'A-', 'B+', 'B', 'B-',
            'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'],
            difficulty: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            classNum: 0,
            quarter: 0,
            quarterLabel: ['Fall', 'Winter', 'Spring', 'Summer'],
            formRules: {
                validateClass(x) {
                    if (x > 99 && x < 700) {
                        return true
                    }
                    return 'Sorry that is not a valid class number'
                },
                validateYear(x) {
                    if (x > 1980 && x < (new Date()).getFullYear()) {
                        return true
                    }
                    return 'Sorry that is not a valid date'
                },
            },
            major: [],
            yearTaken: '',
            review: '',
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
