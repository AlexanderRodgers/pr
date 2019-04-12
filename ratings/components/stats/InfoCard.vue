<template>
    <div>
        <info-header 
            :mVal="stats.mVal"
            :mHeader="stats.mHeader"
            :mSubheader="stats.mSubheader"
            :bgColor="stats.bgColor" />
        <subheader 
            :subheadingImage="stats.subheadingImage"
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

    props: {
        stats: {
            Type: Object,
            required: true,
        }
    },

    mounted() {
    //   if(this.gpa < 3.0) {
    //      this.subheading = 'Mostly Negative'
    //      this.color = 'red'
    //   } else {
    //      this.subheading = 'Mostly Positive'
    //      this.color = 'green'
    //   }
   }
}
</script>

<style>

</style>
