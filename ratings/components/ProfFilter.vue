<template>
  <div class="text-xs-center">
    <v-menu offset-y>
      <template v-slot:activator="{ on }">
        <v-btn
          color="primary"
          dark
          v-on="on"
        >
          {{ filterSelection ? filterSelection : 'Apply Filter' }}
        </v-btn>
      </template>
      <v-list>
        <v-list-tile
          v-for="(item, index) in items"
          :key="index"
          @click="updateFilter(item)"
        >
          <v-list-tile-title>{{ item.title }}</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-menu>
  </div>
</template>

<script>
  export default {

    data() {
      return {
        items: [
          { id: 1, title: 'Professor Rating' },
          { id: 2, title: 'Difficulty' },
          { id: 3, title: 'Class Number' },
        ],
        filterSelection: '',
      }
    }, 

    methods: {
        
        updateFilter(item) {
          console.log(item)
          this.filterSelection = item.title
          this.$emit('selection', item.id)
        },
    }
  }
</script>


<style>

</style>
