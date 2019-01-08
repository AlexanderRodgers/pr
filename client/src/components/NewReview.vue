<template>
    <v-form>
        <v-container>
            <h2>Rate your professor</h2>
            <v-select
                :items="rating"
                label="Professor Rating"
                required
            />
            <h3>How difficult was the course</h3>
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
                <v-flex xs12 sm4 md2 >
                    <v-text-field
                        v-model="classNum"
                        label="Class Number"
                        :rules="[formRules.validateClass(classNum)]"
                        mask="###"
                        required
                    />
                </v-flex>
                <v-flex xs12 sm6 md3 >
                    <v-select
                        :items="major"
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
            
            <v-text-field
                label="Year Taken"
                v-model="yearTaken"
                mask="####"
                :rules="[formRules.validateYear(yearTaken)]"/>
            <v-textarea
                v-model="review"
                auto-grow
                label="Review"
                placeholder="John Smith is a wonderful teacher!"
                counter="10000"/>
            <v-spacer></v-spacer>
            <v-btn color="primary">Submit</v-btn>
        </v-container>
    </v-form>
</template>

<script>
export default {
    data() {
        return {
            rating: ['A+', 'A', 'A-', 'B+', 'B', 'B-',
                    'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'],
            classGrade: ['A+', 'A', 'A-', 'B+', 'B', 'B-',
            'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'],
            difficulty: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            classNum: 0,
            quarter: 0,
            quarterLabel: ['Fall', 'Winter', 'Spring', 'Summer'],
            formRules: {
                validateClass: function(x) {
                    if (x > 99 && x < 700) {
                        return true
                    }
                    return 'Sorry that is not a valid class number'
                },

                validateYear: function(x) {
                    if (x > 1980 && x < (new Date()).getFullYear()) {
                        return true
                    }
                    return 'Sorry that is not a valid date'
                },
            },
            major: [
                'Computer Science', 'Computer Engineering', 'Electrical Engineering'
            ],
            yearTaken: '',
            review: '',
        }
    },

    methods: {
        toggleQuarterButtons(quarter) {
            // 0 == Fall and numbers increase from there in order of season.   
        }
    }
}
</script>

<style>

</style>
