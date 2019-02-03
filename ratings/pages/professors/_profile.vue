<template>
    <div>
        <h1>DYNAMIC</h1>
        <h2>{{data}}</h2>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    async asyncData({ params }) {
    // return {data: params}
    return axios.get(`http://localhost:8000/api/professors/${params.profile}`)
        .then((res) => {
            return { data: res.data}
        })
    }
}
</script>

<style>

</style>
