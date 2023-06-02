<template>
  <UploadFile />
</template>

<script>
import { defineComponent, onMounted } from "vue";

// Components
import UploadFile from "../components/UploadFile.vue";
import api from "../api";

export default defineComponent({
  name: "HomeView",
  components: {
    UploadFile,
  },
  setup() {
    onMounted(() => {
      api
        .get("/")
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.error(error);
        });
    });
  },
});
</script>
