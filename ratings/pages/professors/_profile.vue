<template>
    <div>
        <h1>{{data.first_name + " " + data.last_name}}</h1>
        <h3>{{data}}</h3>
        <gpa :gpa="data.gpa"/>
    </div>
</template>

<script>
import axios from 'axios'
import Gpa from '~/components/stats/Gpa'

export default {

    components: {
        Gpa,
    },

    async asyncData({ params }) {
    // return {data: params}
    return axios.get(`http://localhost:8000/api/professors/${params.profile}`)
        .then((res) => {
            return { data: res.data }
        })
    },

    methods: {

    }
}
</script>

<style>

</style>
   