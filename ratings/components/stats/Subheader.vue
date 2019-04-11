<template>
    <v-card>
        <v-container fluid class="my-container">
            <v-layout row align-center>
                <v-flex shrink>
                    <v-icon xs1 class="pa-1" size="25">
                        {{ subheadingImage }}
                    </v-icon>
                </v-flex>
                <v-flex class="text-xs-left sub-text grey--text" grow>
                    {{ subheading }}
                </v-flex>
            </v-layout>
        </v-container>
    </v-card>
</template>

<script>
export default {
    props: {
        subheading: {
            Type: String,
            required: false,
            default: '',
        },

        subheadingImage: {
            Type: String,
            required: false,
            default: '',
        }
    }

}
</script>
<style scoped>
.my-container {
    margin: 0;
    padding: 0;
}   

.sub-text {
    margin-left: 5px;
}
</style>
