<template>
    <div>
        <h1>DYNAMIC</h1>
        <h2>{{data}}</h2>
    </div>
</template>

<script>
export default {
    async asyncData({ params }) {
        try {
            return {data: params}
        } catch (e) {
            error({ message: "you can't do that.", statusCode: 404})
        }
    }
}
</script>

<style>

</style>
