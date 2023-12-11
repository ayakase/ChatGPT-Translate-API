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
export default {
  data: () => ({
    color: "green",
    files: [
      {
        name: "document.docx",
        time: "27-8-2022",
        size: "2.5 MB",
      },
      {
        name: "image.jpg",
        time: "9-6-2023",
        size: "1.2 MB",
      },
      {
        name: "presentation.ppt",
        time: "18-2-2023",
        size: "4.8 MB",
      },
      {
        name: "spreadsheet.xlsx",
        time: "3-11-2022",
        size: "800.0 KB",
      },
      {
        name: "music.mp3",
        time: "21-7-2023",
        size: "3.6 MB",
      },
      {
        name: "video.mp4",
        time: "10-4-2023",
        size: "25.0 MB",
      },
      {
        name: "archive.zip",
        time: "5-9-2022",
        size: "6.7 MB",
      },
      {
        name: "database.db",
        time: "12-12-2022",
        size: "50.0 MB",
      },
      {
        name: "code.py",
        time: "8-1-2023",
        size: "75.0 KB",
      },
      {
        name: "text.txt",
        time: "30-5-2023",
        size: "12.0 KB",
      },
      {
        name: "presentation2.ppt",
        time: "17-9-2022",
        size: "3.4 MB",
      },
      {
        name: "image2.jpg",
        time: "29-11-2022",
        size: "2.8 MB",
      },
    ],
  }),
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
