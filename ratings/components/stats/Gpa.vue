<template>
   <v-card dark color="green">
      <v-layout align-center justify-center row fill-height>
         <div class="sm6 sx6 flex">
            <div class="layout column ma-0 justify-center align-center white--text"
               :style="{ color: color }">
               <h1><b>{{ gpa }}</b></h1>
            </div>
         </div>
         <v-divider light vertical inset></v-divider>
         <div class="sm6 xs6 flex text-sm-center py-3 white--text" :class="color">
            <div class="headline">GPA</div>
            <span class="caption">{{ subheading }}</span>
         </div>
      </v-layout>
   </v-card>
</template>

<script>
export default {
   props: {
      gpa: Number,
   },

   data() {
      return {
         subheading: '',
         color: '',
      }
   },

   mounted() {
      if(this.gpa < 3.0) {
         this.subheading = 'Mostly Negative'
         this.color = 'red'
      } else {
         this.subheading = 'Mostly Positive'
         this.color = 'green'
      }
   }
}
</script>

<style>

</style>
