<template>
    <v-card
        class="stats-card"
    >
        <card-image
            mainIcon="show_chart"
        />
        <div class="text-xs-right card-text">
            <p
                class="category grey--text font-weight-light"
            />
            <h3
                class="title display-1 font-weight-light">
                My Value <small>Smaller value</small>
            </h3>
        </div>
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
    right: 0;
    width: 100%;
}

</style>
