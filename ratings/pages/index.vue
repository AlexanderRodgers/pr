<template>
  <div>
    <search/>
  </div>
</template>

<script>
import profs from '~/mixins/profs.js'
import Search from '~/components/Search'
export default {
  components: {
    Search,
  },

  mixins: [profs],
}
</script>
