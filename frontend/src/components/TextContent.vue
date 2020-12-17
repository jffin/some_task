<template>
  <v-container>
    <loader v-if="isLoading" />
    <v-list v-else>
      <template v-for="(item, index) in textSentences">
        <v-list-item :key="index" @click="getSimilar(item)">
          <v-list-item-content>
            <v-list-item-title>{{ item }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>
    <sentences-dialog :similar-sentences="similarSentences" v-model="dialog" />
  </v-container>
</template>

<script>
import Loader from './Loader';
import SentencesDialog from './SentencesDialog';

import textClient from '../text-client'

export default {
  name: 'TextContent',
  components: {
    SentencesDialog,
    Loader,
  },
  props: {
    textSentences: {
      type: Array,
      required: true,
    },
    slug: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      dialog: false,
      similarSentences: [],
      isLoading: false,
    }
  },
  methods: {
    async getSimilar(sentence) {
      this.toggleLoading();
      this.similarSentences = await textClient.getSimilarSentences(sentence, this.slug);
      this.dialog = true;
      this.toggleLoading();
    },
    toggleLoading() {
      this.isLoading = !this.isLoading;
    },
  },
}
</script>
