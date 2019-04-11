<template>
    <v-card
        class="stats-card"
        color="green"
    >
        <card-image
            mainIcon="show_chart"
        />
        <v-card-title primary-title class="white--text">
            <h3 class="headline">GPA</h3>
        </v-card-title>
    </v-card>
</template>

<script>
import CardImage from '~/components/helper/CardImage'
export default {
    components: {
        CardImage,
    }
}
</script>

<style scoped>
.stats-card {
    display: flex;
    flex-wrap: wrap;
    position: relative;
}

.card-text {
    display: inline-block;
    padding: 10 10 0 0;
    position: absolute;
    top: 0;
    right: 10;
    width: 100%;
}

</style>
