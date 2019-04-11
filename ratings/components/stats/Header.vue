<template>
   <v-card dark color="green">
      <v-layout align-center justify-center row fill-height>
         <div class="sm3 sx3 flex">
            <div class="layout column ma-0 justify-center align-center white--text"
               :style="{ color: bgColor }">
               <h1><b>{{ mVal }}</b></h1>
            </div>
         </div>
         <div class="sm6 xs6 flex text-sm-center py-3 white--text" :class="bgColor">
            <div class="headline">{{ mHeader }}</div>
            <span class="caption">{{ mSubheader }}</span>
         </div>
      </v-layout>
   </v-card>
</template>

<script>
export default {
   props: {
      mVal: {
         Type: String,
         required: true,
      },

      mHeader: {
         Type: String,
         required: true,
      },

      mSubheader: {
         Type: String,
         required: false,
         default: ''
      },

      bgColor: {
         Type: String,
         required: true,
         default: ''
      }
      
   },
   
}
</script>

<style>

</style>
