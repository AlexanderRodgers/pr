<template>
    <v-container>
        <v-layout>
            <v-flex xs3>
                <profile-info/>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import ProfileInfo from '~/apps/profileInfo'
export default {

    components: {
        ProfileInfo,
    }

}
</script>

<style>

</style>
