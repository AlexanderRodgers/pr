<template>
    <form action="">
        <v-text-field
            v-model="firstName"
            label="First Name"
            required
        />
        <v-text-field
            v-model="lastName"
            label="Last Name"
            required
        />
        <v-text-field
            v-model="password"
            :append-icon="showPassword ? 'visibility' : 'visibility_off'"
            :type="showPassword ? 'text' : 'password'"
            label="Password"
            @click:append="showPassword = !showPassword"
        />
    </form>    
</template>

<script>
export default {
    data() {
        return {
            showPassword: false,
        }
    }
}
</script>

<style>

</style>
