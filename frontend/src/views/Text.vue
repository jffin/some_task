<template>
  <div class="text">
    <text-content :text-sentences="textSentences" :slug="slug" />
  </div>
</template>

<script>
import TextContent from '../components/TextContent';

import { mapState } from 'vuex';

export default {
  components: {TextContent},
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
  watch: {
    '$route': 'fetchInfo',
  },
  methods: {
    fetchInfo() {
      this.$store.dispatch('getText', this.slug);
    },
  },
  mounted() {
    this.fetchInfo();
  },
  computed: {
    ...mapState({textSentences: state => state.text})
  },
}
</script>
