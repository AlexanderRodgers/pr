<template>
   <v-card>
      <v-layout align-center justify-center row fill-height>
         <div class="sm6 sx6 flex">
            <div class="layout column ma-0 justify-center align-center"
               :style="{ color: color }">
               <h1><b>{{ numReviews }}</b></h1>
            </div>
         </div>
         <div class="sm6 xs6 flex text-sm-center py-3 white--text"
               :style="{ background: color }">
            <div class="headline">Reviews</div>
            <span class="caption"> 95th percentile of all reviews </span>
         </div>
      </v-layout>
   </v-card>
</template>

<script>
export default {
   props: {
      numReviews: Number,
   },

   data() {
      return {
         color: '#800080',
      }
   },
}
</script>

<style>

</style>
