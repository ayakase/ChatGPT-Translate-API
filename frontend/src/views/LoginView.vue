<template>
  <div class="login-container">

    <v-sheet width="300" class="mx-auto">
      <v-form fast-fail @submit.prevent>
        <v-text-field
          label="Run email"
        ></v-text-field>

        <v-text-field
          label="password"
        ></v-text-field>

        <v-btn type="submit" block class="mt-2 login-button">Submit</v-btn>
      </v-form>
    </v-sheet>
  </div>
</template>
<script>
export default {};
</script>

<style scoped>
.login-container {
  margin: auto;
  padding: auto;
  margin-top: 5rem;
}
.login-button {
    border-radius: 2rem;
}
</style>
