<template>
  <div>
    <h1 class="text-center header deep-purple--text darken-2">Enter Your Text Please</h1>
    <v-form class="px-3">
      <v-textarea
          class="text-adding purple darken-4 rounded-lg"
          label="Text"
          counter
          clearable-icon
          auto-grow
          hint="put here your long amazing text"
          v-model="content"
      />
      <v-btn
          text
          class="purple darken-4 mx-3 mt-3 float-right"
          @click="addNewText"
      >
        Save Text
      </v-btn>
    </v-form>
    <v-row justify="center">
      <v-dialog
          v-model="dialog"
          persistent
          max-width="290"
      >
        <v-card>
          <v-card-text>
            <div class="text-center pt-5">
              {{ result }}
            </div>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
                class="purple darken-4 mx-3 mt-3 float-right"
                text
                @click="dialog = false"
            >
              OK
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>

<script>
import textClient from '../text-client';

export default {
  name: 'TextInput',
  data() {
    return {
      content: '',
      result: '',
      dialog: false,
    }
  },
  methods: {
    async addNewText() {
      if (this.content) {
        const data = await this.sendRequest();
        this.result = data.msg;
        this.dialog = true;
        // store.addTextAction(data.text);
      } else {
        this.result = 'Enter A Text Please!';
        this.dialog = true;
      }
    },
    async sendRequest() {
      return await textClient.addNewText(this.content);
    }
  },
}
</script>
