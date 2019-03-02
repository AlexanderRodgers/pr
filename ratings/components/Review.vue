<template>
   <v-container>
      <v-layout>
         <v-flex xs12 md3>
            <v-card>
               <v-card-text>
                  User: {{ review.user }} <br/>
                  Professor Rating: {{ review.rating}} <br/>
                  Class Grade: {{ review.class_grade }} <br/>
                  Class Difficulty: {{ review.difficulty }} <br/>
                  {{ translateQuarter(review.quarter) }} Quarter<br/>
               </v-card-text>
            </v-card>
         </v-flex>
         <v-flex d-flex>
            <v-card>
               <v-card-text>
                  {{review.review}}
               </v-card-text>
            </v-card>
         </v-flex>
      </v-layout>
   </v-container>
</template>

<script>
export default {
   props: {
      review: Object,
   },

   methods: {
      translateQuarter(num) {
         switch (num) {
            case 0: return "Fall"
            case 1: return "Winter"
            case 2: return "Spring"
            case 3: return "Summer"
            
         }
      }
   }
}
</script>

<style>

</style>
