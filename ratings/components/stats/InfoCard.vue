<template>
    <div v-if="loaded">
        <info-header 
            :m-val="stats.mVal"
            :m-header="stats.mHeader"
            :m-subheader="stats.mSubheader"
            :bg-color="stats.bgColor" />
        <subheader 
            :subheading-image="stats.subheadingImage"
            :subheading="stats.subheading"/>
    </div>
</template>

<script>
import InfoHeader from '~/components/stats/Header'
import Subheader from '~/components/stats/Subheader'
export default {
    components: {
        InfoHeader,
        Subheader
    },

    data() {
        return {
            loaded: false,
        }
    },

    props: {
        stats: {
            Type: Object,
            required: true,
        }
    },

    mounted() {
        this.loaded = true
   }
}
</script>

<style>

</style>
