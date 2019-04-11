<template>
    <div>
        <info-header mVal="3.5" mHeader="GPA" mSubheader="mostly positive" bgColor="green" />
        <subheader subheadingImage="trending_up" subheading="Trending upwards"/>
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
