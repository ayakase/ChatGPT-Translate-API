<template>
  <div class="container">
    <h2 class="title">Upload XLSX file here</h2>
    <v-file-input
      show-size
      counter
      v-model="selectedFile"
      :accept="['.xlsx']"
      label="Choose file"
      class="file-input"
    ></v-file-input>
    <v-btn @click="uploadFile()" class="submit-button">Submit</v-btn>
    <v-card
      class="server-prompt"
      :loading="isLoading"
      title="Processing"
      variant="outlined"
    >
      <v-divider></v-divider>
      <div class="message-container">
        <p class="message" v-for="message in messages" :key="message">
          {{ message }}
        </p>
      </div>
    </v-card>
  </div>
</template>

<script>
import { ref } from "vue";
import api from "../api";
import io from "socket.io-client";
import { useToast } from "vue-toast-notification";
import "vue-toast-notification/dist/theme-sugar.css";
import { onMounted } from "vue";
export default {
  setup() {
    const socket = io("http://localhost:5000");
    const message = ref("");
    const selectedFile = ref(null);
    let formtext = ref();
    const isLoading = ref(false);
    let messages = ref(["translating", "translating"]);
    const $toast = useToast();
    const uploadFile = () => {
      if (!selectedFile.value || selectedFile.value.length === 0) {
        $toast.error("No file selected");
        isLoading.value = false;
        return;
      }
      const formData = new FormData();
      console.log(selectedFile.value[0].name);
      isLoading.value = true;
      formData.append("file", selectedFile.value[0]);
      const config = {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      };
      api
        .post("/upload", formData, config)
        .then((response) => {
          console.log(response);
          $toast.success(response.data.message);
        })
        .catch((error) => {
          console.log("Error occurred:", error);
        });
    };
    onMounted(() => {
      socket.on("uploaded", (response) => {
        console.log(response);
        // $toast.success(message.value);
      });
    });
    return {
      selectedFile,
      uploadFile,
      formtext,
      messages,
      isLoading,
    };
  },
};
</script>

<style scoped>
.container {
  padding-top: 2rem;
  margin: auto;
  padding: auto;
  width: 80%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.title {
  margin-bottom: 1rem;
  color: #23aa8f;
}
.file-input {
  width: 60%;
}
.submit-button {
  width: 6rem;
}
.server-prompt {
  margin-top: 2rem;
  width: 60%;
  height: 30rem;
  padding-left: 1rem;
  overflow: hidden;
}
.message-container {
  height: 88%;
  overflow: scroll;
}
::-webkit-scrollbar {
  display: none;
}
</style>
