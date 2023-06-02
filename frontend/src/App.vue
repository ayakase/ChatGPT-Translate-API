<template>
  <v-app>
    <v-bottom-navigation>
      <div class="logo-container">
        <img class="company-logo" src="../src/assets/company-logo.jpg" alt="">
        <img class="chatgpt-logo" src="../src/assets/chatgpt.png" alt="">

      </div>
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

<style>
v-bottom-navigation {
  display: flex;
  justify-content: space-between;
}

.logo-container {
  margin-right: auto;
  margin-left: 0;

}

.company-logo {
  width: 18rem;
  /* adjust the width as needed */
}

.chatgpt-logo {
  width: 9rem;
  margin-bottom: 0.5rem;
  /* adjust the width as needed */
}

.bottom-navigation v-btn {
  flex-grow: 1;
  text-align: center;
}
</style>
