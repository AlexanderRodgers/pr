<template>
    <div>
        <v-btn fab color="primary" @click="dialog = true">
            <v-icon>group_add</v-icon>
        </v-btn>
        <!-- TODO: change max-width to fit to all screens better -->
    <v-dialog v-model="dialog" max-width="35%">
        <v-card class="elevation-12">
            <v-toolbar dark color="primary title">Add a Professor</v-toolbar>
            <v-form @submit.prevent="onSubmit" ref="form" v-model="valid" lazy-validation>
                <vue-recaptcha
                    ref="invisibleRecaptcha"
                    @verify="onVerify"
                    @expired="onExpired"
                    size="invisible"
                    :sitekey="sitekey"
                />
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
                        <v-btn type="submit" color="primary">Add</v-btn>
                </v-card-actions>    
            </v-form>
        </v-card>
    </v-dialog>
    </div>
</template>

<script>
import axios from 'axios'
import VueRecaptcha from 'vue-recaptcha'
export default {

    components: {
        VueRecaptcha,
    },
    
    data() {
        return {
            sitekey: '6LeEdZoUAAAAAAbL_j7ewtNS_wvhjDUyDj0IkMgP',
            dialog: false,
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

        onVerify(response) {
            console.log('Verify', response)
            this.$refs.invisibleRecaptcha.reset();
        },

        onSubmit() {
            console.log('submitted.')
            this.$refs.invisibleRecaptcha.execute()
            
        },

        onExpired() {
            console.log('expired.')
        },

        submit() {
            if(this.dev_mode) {
                if(!this.email.includes('@calpoly.edu')) {
                    this.email += '@calpoly.edu'
                }
                let postData = {
                    first_name: this.firstName,
                    last_name: this.lastName,
                    email: this.email ? this.email : undefined,
                    major: this.major ? this.major : undefined
                }
                axios.post(this.dev + '/api/professors/', postData)
                .then(res => {
                    if (res.status === 201) {
                        this.$emit('validated', postData)
                    } else if (res.status === 400) {
                        this.$emit('validated', {})
                    }
                    console.log(res)
                }).catch(e => {
                    console.log(e)
                })
            }
            this.snackbar = false
            this.dialog = false
        }
    },

    mounted() {
        axios.get(this.dev + '/api/majors/')
            .then(res => {
                for (let major of res.data) {
                    this.majorList.push(major)
                }
            })
        let recaptchaScript = document.createElement('script')
        recaptchaScript.setAttribute('src', 'https://www.google.com/recaptcha/api.js?onload=vueRecaptchaApiLoaded&render=explicit   ')
        recaptchaScript.async = true
        recaptchaScript.defer = true
        document.head.appendChild(recaptchaScript)
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
