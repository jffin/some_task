<template>
  <v-data-table
      :headers="headers"
      :keys="keys"
      :items="texts"
      :items-per-page="25"
      class="elevation-1"
      :loading="isLoading"
      loading-text="Loading... Please wait"
  >
    <template v-slot:item.text_content="{ item }">
      <router-link
          router
          :to="{name: 'Text', params: {slug: item.slug}}"
          class="text-decoration-none text-uppercase white--text pl-5"
      >
        {{ item.text_content }}
      </router-link>
    </template>
  </v-data-table>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'TextsPanel',
  data() {
    return {
      isLoading: false,
      keys: [
        'text_content',
        'updated',
        'created',
      ],
      headers: [
        {
          text: 'Text Content',
          align: 'start',
          value: 'text_content',
        },
        {text: 'Updated', value: 'updated'},
        {text: 'Created', value: 'created'},
      ],
    }
  },
  mounted() {
    this.$store.dispatch('getTexts');
  },
  computed: {
    ...mapState({texts: state => state.texts}),
  },
  methods: {
    toggleLoading() {
      this.isLoading = !this.isLoading;
    },
  },
}
</script>
