<template>
  <v-row justify="center" class="mt-5">
    <v-list three-line>
      <template v-for="(item, index) in texts">
        <v-list-item :key="index" router :to="{name: 'Text', params: {slug: item.slug}}">
          <v-list-item-content>
            <v-list-item-title>{{ item.content }}</v-list-item-title>
            <v-list-item-subtitle>{{ item.updated }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>
  </v-row>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'TextsPanel',
  mounted() {
      this.$store.dispatch('getTexts');
  },
  computed: {
    ...mapState({texts: state => state.texts})
  },
}
</script>
