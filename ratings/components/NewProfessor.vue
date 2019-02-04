<template>
    <v-container fluid fill-height>
        <v-layout align-center justify-center>
            <v-card class="elevation-12">
                <v-toolbar dark color="primary title">Add a Professor</v-toolbar>
                <v-form ref="form" v-model="valid" lazy-validation>
                    <v-flex class="form-field">
                        <v-text-field
                        v-model="firstName"
                        label="First Name"
                        :rules="[formRules.hasContent(firstName), formRules.hasNumber(lastName)]"
                        required
                        outline
                        />
                    </v-flex>
                    <v-flex class="form-field">
                        <v-text-field
                        v-model="lastName"
                        label="Last Name"
                        :rules="[formRules.hasContent(lastName), formRules.hasNumber(lastName)]"
                        required
                        outline
                        />
                    </v-flex>
                    <v-flex class="form-field">
                        <v-text-field
                        v-model="email"
                        label="Professor Email"
                        suffix="@calpoly.edu"
                        outline
                        hint="This field is optional"
                        />
                    </v-flex>
                    <v-flex class="form-field">
                        <v-select
                        v-model="major"
                        :items=majorList
                        label="Major"
                        item-text="major"
                        item-value="id"
                        outline
                        />
                    </v-flex>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn @click="validate()" color="info">Submit</v-btn>
                    </v-card-actions>    
                </v-form>
            </v-card>
        </v-layout>

    </v-container>
</template>

<script>
import axios from 'axios'
export default {

    data() {
        return {
            valid: true,
            dev_mode: true,
            firstName: '',
            lastName: '',
            email: '',
            major: '',
            majorList: [],
            dev: 'http://localhost:8000',
            build: '',
            formRules: {
                hasContent(str) {
                    return !!str || 'Cannot submit an empty value'
                },
                hasNumber(str) {
                    var re = /^[A-Za-z]+$/
                    if (re.test(str)) {
                        return !!str || 'Sorry, the name cannot contain a number'
                    }
                },
            }
        }
    },

    methods: {
        validate() {
            if(this.$refs.form.validate()) {
                this.snackbar = true
                this.submit()
            }
        },

        submit() {
            if(this.dev_mode) {
                axios.post(this.dev + '/api/professors/', {
                    first_name: this.firstName,
                    last_name: this.lastName,
                    email: this.email ? this.email : undefined,
                    major: this.major ? this.major : undefined
                }).then(res => {
                    console.log(res)
                }).catch(e => {
                    console.log(e)
                })
            }
        }
    },

    mounted() {
        axios.get(this.dev + '/api/majors/')
            .then(res => {
                for (let major of res.data) {
                    this.majorList.push(major)
                }
            })
    }

}
</script>

<style scoped>

.form-field {
    margin-left: 20px;
    margin-right: 20px;
    margin-top: 20px;
}

</style>