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
  </div>
</template>

<script>
import textClient from '../text-client';

export default {
  name: 'TextInput',
  data() {
    return {
      content: '',
    }
  },
  methods: {
    async addNewText() {
      console.log(this.content);
      if (this.content) {
        return await textClient.addNewText(this.content);
      }
      else {
        alert('Enter A Text Please!')
      }
    }
  }
}
</script>

<style scoped>

</style>
