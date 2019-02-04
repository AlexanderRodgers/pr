<template>
    <div>
        <h1>{{data.first_name + " " + data.last_name}}</h1>
        <h3>{{data}}</h3>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    async asyncData({ params }) {
    // return {data: params}
    return axios.get(`http://localhost:8000/api/professors/${params.profile}`)
        .then((res) => {
            return { data: res.data }
        })
    }
}
</script>

<style>

</style>
   