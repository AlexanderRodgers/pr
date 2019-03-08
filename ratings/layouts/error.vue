<template>
  <div class="container">
    <h1 v-if="error.statusCode === 404">Sorry that page doesn't seem to exist.</h1>
    <h1 v-else>An error occurred</h1>
    <nuxt-link to="/">Let's go back home</nuxt-link>
  </div>
</template>

<script>
export default {
  props: ['error'],
  layout: 'blog' // you can set a custom layout for the error page
}
</script>