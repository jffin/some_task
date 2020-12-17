<template>
  <div>
    <v-row justify="center">
      <v-col cols="12">
        <loader v-if="isLoading" />
        <div v-else>
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
        </div>
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
      </v-col>
    </v-row>
  </div>
</template>

<script>
import Loader from './Loader';

export default {
  name: 'TextInput',
  components: {Loader},
  data() {
    return {
      content: '',
      result: '',
      dialog: false,
      isLoading: false,
    }
  },
  methods: {
    async addNewText() {
      if (this.content) {
        this.toggleLoading();
        this.scrollToTop();
        const result = await this.$store.dispatch('sendText', this.content);
        this.toggleLoading();
        this.handleResult(result);
      } else {
        this.handleResult('Enter A Text Please!');
      }
    },
    handleResult(resultMessage) {
      this.result = resultMessage;
      this.dialog = true;
      this.content = '';
    },
    toggleLoading() {
      this.isLoading = !this.isLoading;
    },
    scrollToTop() {
      window.scrollTo(0, 0);
    },
  },
}
</script>
