<template>
  <v-app>
    <v-app-bar :elevation="3" rounded>
      <template v-slot:prepend>
        <div class="logo-container"></div>
      </template>
      <template v-slot:append>
        <v-btn value="recent" to="/">
          <v-icon>mdi-translate</v-icon>
          Translate
        </v-btn>
        <v-btn value="history" to="/history">
          <v-icon>mdi-history</v-icon>
          History
        </v-btn>
        <v-switch
          v-model="switchValue"
          hide-details
          true-value="Dark"
          false-value="Light"
          color="red-darken-3"
          inset
        ></v-switch>
      </template>
    </v-app-bar>
    <v-main>
      <keep-alive>
        <router-view />
      </keep-alive>
    </v-main>
  </v-app>
</template>
<script>
import { ref } from "vue";

export default {
  setup() {
    let switchValue = ref("Light");
    return { switchValue };
  },
};
</script>
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
