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
    <v-btn @click="downloadFile"> Download</v-btn>
    <v-card
      class="server-prompt"
      :loading="isLoading"
      :title="processStatus"
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

<!-- <script>
import { ref } from "vue";
import api from "../api";
import io from "socket.io-client";
import { useToast } from "vue-toast-notification";
import "vue-toast-notification/dist/theme-sugar.css";
import { onMounted } from "vue";

export default {
  setup() {
    let processStatus = ref("Status");
    const socket = io("http://localhost:5000");
    const selectedFile = ref(null);
    let formtext = ref();
    const isLoading = ref(false);
    let messages = ref([]);
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
        .post("/upload", formData, config, { responseType: "blob" })
        .then((response) => {
          
          this.translateFile = response.data.translated_file;
        })
        .catch((error) => {
          console.log("Error occurred:", error);
        });
    },
    downloadFile = () => {
      window.open('/download/${this.translateFile}', '_blank');
    
    };
    onMounted(() => {
      socket.on("uploaded", (response) => {
        console.log(response);
        $toast.success(response);
        processStatus.value = "Translating";
      });
      socket.on("complete", (response) => {
        console.log(response);
        isLoading.value = false;
        $toast.success(response);
        processStatus.value = "Completed Translation";
      });
      socket.on("process", (response) => {
        console.log(response);
        messages.value.push(response);
      });
    });
    return {
      selectedFile,
      uploadFile,
      formtext,
      messages,
      isLoading,
      downloadFile,
      processStatus,
    };
  },
};
</script> -->

<script>
import { ref } from "vue";
import api from "../api";
import io from "socket.io-client";
import { useToast } from "vue-toast-notification";
import "vue-toast-notification/dist/theme-sugar.css";
import { onMounted } from "vue";

export default {
  setup() {
    let processStatus = ref("Status");
    const socket = io("http://localhost:5000");
    const selectedFile = ref(null);
    let formtext = ref();
    const isLoading = ref(false);
    let messages = ref([]);
    const $toast = useToast();
    const translateFile = ref(""); // Create a reactive reference for translateFile

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
        .post("/upload", formData, config, { responseType: "blob" })
        .then((response) => {
          translateFile.value = response.data.translated_file; // Update the translateFile value
        })
        .catch((error) => {
          console.log("Error occurred:", error);
        });
    };

const downloadFile = () => {
  api
    .post(`/download/${translateFile.value}`, null, { responseType: "blob" })
    .then((response) => {
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", translateFile.value);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    })
    .catch((error) => {
      console.log("Error occurred:", error);
    });
};


    onMounted(() => {
      socket.on("uploaded", (response) => {
        console.log(response);
        $toast.success(response);
        processStatus.value = "Translating";
      });
      socket.on("complete", (response) => {
        console.log(response);
        isLoading.value = false;
        $toast.success(response);
        processStatus.value = "Completed Translation";
      });
      socket.on("process", (response) => {
        console.log(response);
        messages.value.push(response);
      });
    });

    return {
      selectedFile,
      uploadFile,
      formtext,
      messages,
      isLoading,
      downloadFile,
      processStatus,
      translateFile, // Expose the translateFile reference
    };
  },
};
</script>

<style scoped>
.container {
  padding-top: 1rem;
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
  color: white;
  margin-top: 1rem;
  width: 60%;
  height: 28rem;
  overflow: hidden;
  background-color: rgb(61, 61, 61);
}

.message-container {
  height: 90%;
  overflow: scroll;
}

.message {
  margin-top: 0.2rem;
  color: white;
  padding-left: 1rem;
}

::-webkit-scrollbar {
  display: none;
}
</style>
