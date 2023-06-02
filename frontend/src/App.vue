<template>
  <v-app>
    <v-bottom-navigation>
      <v-btn value="recent" to="/">
        <v-icon>mdi-history</v-icon>

        Recent
      </v-btn>

      <v-btn value="favorites" to="/about">
        <v-icon>mdi-heart</v-icon>

        Favorites
      </v-btn>

      <v-btn value="nearby">
        <v-icon>mdi-map-marker</v-icon>

        Nearby
      </v-btn>
    </v-bottom-navigation>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
};
</script>
