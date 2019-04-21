<template>
   <v-container>
      <v-layout>
         <v-flex xs3 md3>
            <v-card class="background review-info">
               <v-card-text>
                  {{ review.major }} {{ review.class_num }}  <br/>
                  Class Grade: {{ review.class_grade }} <br/>
                  Class Difficulty: {{ review.difficulty }} <br/>
                  {{ translateQuarter(review.quarter) }} Quarter<br/>
               </v-card-text>
            </v-card>
         </v-flex>
         <v-flex d-flex>
            <v-card class="background">
               <v-card-text>
                  <h4>{{ review.user }} <span style="float:right;">{{ review.rating }}</span></h4>
                  <v-divider/>
                  {{review.review}}
               </v-card-text>
            </v-card>
         </v-flex>
      </v-layout>
   </v-container>
</template>

<script>
import MajorApi from '~/services/api/majors.js'
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
   },

   mounted() {
      MajorApi.getMajor(this.review.major)
         .then(res => {
            this.review['major'] = res.abbreviation
         })
   }
}
</script>

<style scoped>
.review-info {
   margin-right: 5px;
}

</style>
