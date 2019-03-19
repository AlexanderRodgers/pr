<template>
    <div>
        <search/>
        <!-- <new-professor/> -->
    </div>
</template>

<script>
import axios from 'axios'
import NewProfessor from '~/components/NewProfessor'
import Search from '~/components/Search'
import NewReview from '~/components/NewReview'

export default {
    components: {
        Search,
        NewProfessor,
        NewReview,
    },

    data() {
        return {
            keys: '',
            codeEntered: false,
        }
    },

    methods: {
        getCode(event) {
            this.keys += event.keyCode;
            if (this.keys.length > 100) {
                this.keys = ''
            }
            this.codeEntered = this.keys.includes('3838404037393739666513')
        }
    },

    watch: {
        codeEntered() {
            window.location.replace("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        }
    },

    mounted() {
        window.addEventListener("keyup", e => {
            this.getCode(e)
        });
    }
}
</script>

<style>

</style>
