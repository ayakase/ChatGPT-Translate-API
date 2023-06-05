<template>
  <v-app>
    <v-app-bar :elevation="3" rounded>
      <template v-slot:prepend>
        <div class="logo-container">
          <img
            class="company-logo"
            src="../src/assets/company-logo.jpg"
            alt=""
          />
          <img class="chatgpt-logo" src="../src/assets/chatgpt.png" alt="" />
        </div>
      </template>
      <template v-slot:append>
        <v-btn value="recent" to="/">
          <v-icon>mdi-translate</v-icon>
          Translate
        </v-btn>
        <v-btn value="favorites" to="/about">
          <v-icon>mdi-history</v-icon>
          History
        </v-btn>
        <v-btn value="nearby">
          <v-icon>mdi-map-marker</v-icon>
          Nearby
        </v-btn>
        <v-btn icon="mdi-dots-vertical"></v-btn>
      </template>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>
<style>
v-app-bar {
  background-color: rebeccapurple;
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
