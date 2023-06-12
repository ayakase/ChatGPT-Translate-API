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
          @click="toggleTheme"
          :prepend-icon="iconStatus"
          color="orange"
          inset
        >
          <v-tooltip activator="parent" location="bottom"
            >Toggle Dark Mode</v-tooltip
          >
        </v-switch>
        <div class="spacer"></div>

        <v-btn value="home" to="/">
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
import { ref, onMounted } from "vue";
import { useTheme } from "vuetify";

export default {
  setup() {
    let switchValue = ref();
    const theme = useTheme();
    let iconStatus = ref();
    function toggleTheme() {
      theme.global.name.value = theme.global.current.value.dark
        ? "light"
        : "dark";
      localStorage.setItem("theme", theme.global.name.value);
      if (localStorage.getItem("theme") == "light") {
        iconStatus.value = "mdi-white-balance-sunny";
      } else if (localStorage.getItem("theme") == "dark") {
        iconStatus.value = "mdi-moon-waxing-crescent";
      }
    }
    onMounted(() => {
      theme.global.name.value = localStorage.getItem("theme") || "light";
      console.log(localStorage.getItem("theme"));
      if (localStorage.getItem("theme") == "light") {
        switchValue.value = false;
        iconStatus.value = "mdi-white-balance-sunny";
      } else if (localStorage.getItem("theme") == "dark") {
        switchValue.value = true;
        iconStatus.value = "mdi-moon-waxing-crescent";
      } else {
        switchValue.value = false; // Default to light theme if no localStorage value is set
      }
    });
    return {
      switchValue,
      theme,
      toggleTheme,
      iconStatus,
    };
  },
};
</script>
<style>
v-app-bar {
  background-color: rebeccapurple;
}

.logo-container {
  display: flex;
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
