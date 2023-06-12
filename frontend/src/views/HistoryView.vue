<template>
  <v-container>
    <v-row justify="space-around">
      <v-card width="50rem">
        <v-card-text>
          <div class="font-weight-bold ms-1 mb-2">History</div>
          <v-timeline density="compact" align="center" width="100%">
            <v-timeline-item
              v-for="file in files"
              :key="file.time"
              :dot-color="color"
              size="x-small"
              width="100%"
            >
              <v-card class="each-file">
                <div class="file-container">
                  <div class="text-container">
                    <strong style="font-size: 18px">{{ file.name }}</strong>
                    <div>{{ file.time }}</div>
                    <div style="color: gray">{{ file.size }}</div>
                  </div>
                  <v-btn class="download-button" variant="text"
                    ><v-icon>mdi-cloud-download</v-icon></v-btn
                  >
                </div>
              </v-card>
            </v-timeline-item>
          </v-timeline>
        </v-card-text>
      </v-card>
    </v-row>
  </v-container>
</template>
<script>
import { onMounted } from "vue";
import api from "../api";

export default {
  setup() {
    onMounted(() => {
      api.get("/history").then((response) => {
        console.log(response.data);
      });
    });
  },
};
</script>

<style scoped>
.each-file {
  width: 100%;
  height: 5rem;
  padding: 0.5rem;
}

.file-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.download-button {
  height: 3rem;
  margin-top: 0.5rem;
  border-radius: 2rem;
  font-size: x-large;
  color: rgb(224, 34, 72);
}
</style>
