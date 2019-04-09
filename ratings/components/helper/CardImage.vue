<template>
    <v-card
        class="pa-3 card-image"
        elevation="3"
        color="green"
        dark
    >
        <v-icon
            size="40"
        >
            {{ mainIcon }}
        </v-icon>
    </v-card>
</template>

<script>
export default {

    props: {
        mainIcon: {
            type: String,
            required: true
        }
    }

}
</script>

<style scoped>
.card-image {
    display: inline-block;
    border-radius: 4px;
    flex: 0 1 auto;
    margin-top: 0;
    margin-left: 0;
    margin-right: auto;
    margin-bottom: 0 !important;
    max-width: auto;
    padding: 0 16px 0;
}

</style>
