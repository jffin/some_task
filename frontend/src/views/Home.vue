<template>
  <div class="home">
    <v-container>
      <text-input />
    </v-container>
    <v-container>
      <texts-panel />
    </v-container>
  </div>
</template>

<script>
import TextInput from '../components/TextInput.vue';
import TextsPanel from '../components/TextsPanel.vue';

export default {
  name: 'Home',
  components: {
    TextInput,
    TextsPanel,
  },
}
</script>
