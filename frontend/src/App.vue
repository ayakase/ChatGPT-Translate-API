<template>
  <v-app>
    <v-app-bar :elevation="3" rounded>
      <template v-slot:prepend>
        <div class="logo-container">
          <img
            class="company-logo"
            src="../src/assets/company-logo.png"
            alt=""
          />
          <div class="spacer"></div>

          <!-- <img class="chatgpt-logo" src="../src/assets/chatgpt.png" alt="" /> -->
        </div>
      </template>
      <template v-slot:append>
        <v-switch
          v-model="switchValue"
          hide-details
          true-value="Dark"
          false-value="Light"
          @click="toggleTheme"
          color="orange"
          inset
        >
          <v-tooltip activator="parent" location="bottom"
            >Toggle Dark Mode</v-tooltip
          >
        </v-switch>
        <div class="spacer"></div>

        <v-btn value="recent" to="/">
          <v-icon>mdi-translate</v-icon>
          Translate
        </v-btn>
        <div class="spacer"></div>

        <v-badge color="error" content="12">
          <v-btn value="history" to="/history">
            <v-icon>mdi-history</v-icon>
            History
            <v-tooltip activator="parent" location="bottom"
              >File that you have translated</v-tooltip
            >
          </v-btn>
        </v-badge>
        <div class="spacer"></div>
      </template>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>
<script>
import { ref } from "vue";
import { useTheme } from "vuetify";

export default {
  setup() {
    let switchValue = ref("Light");
    const theme = useTheme();

    return {
      switchValue,
      theme,
      toggleTheme: () =>
        (theme.global.name.value = theme.global.current.value.dark
          ? "light"
          : "dark"),
    };
  },
};
</script>
<style>
v-app-bar {
  background-color: rebeccapurple;
}

.logo-container {
  display:flex;
  flex-direction: row;
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
.spacer {
  margin: 1rem;
}
</style>
