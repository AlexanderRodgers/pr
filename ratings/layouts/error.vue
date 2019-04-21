<template>
<v-container fluid>
  <v-layout row align-center>
    <h1 v-if="error.statusCode === 404">Sorry that page doesn't seem to exist.</h1>
    <h1 v-else>An error occurred</h1>
  </v-layout> 
    <nuxt-link to="/">Let's go back home</nuxt-link>
</v-container>
</template>

<script>
export default {
  props: ['error'],
  layout: 'blog' // you can set a custom layout for the error page
}
</script>