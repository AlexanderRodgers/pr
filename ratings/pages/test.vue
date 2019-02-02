<template>
    <div>
        <search/>
        <new-professor/>
    </div>
</template>

<script>
import NewProfessor from '~/components/NewProfessor'
import Search from '~/components/Search'
export default {
    components: {
        Search,
        NewProfessor,
    }
}
</script>

<style>

</style>
