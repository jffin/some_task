<template>
  <v-row justify="center">
    <v-dialog
        :value="value"
        fullscreen
        hide-overlay
        transition="dialog-bottom-transition"
        @input="$emit('input', false)"
    >
      <v-card>
        <v-toolbar
            dark
            color="primary"
        >
          <v-btn
              icon
              dark
              @click="$emit('input', false)"
          >
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title>Similar Sentences</v-toolbar-title>
        </v-toolbar>
        <v-card-text>
          <sentences :similar-sentences="similarSentences" />
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import Sentences from './SimilarSentences';

export default {
  name: 'SimilarSentences',
  components: {Sentences},
  props: {
    similarSentences: {
      type: Array,
      required: true,
    },
    value: {
      type: Boolean,
      required: true,
    },
  },
  watch: {
    '$route': {
      handler() {
        this.$emit('input', false)
      }
    },
  },
}
</script>>
