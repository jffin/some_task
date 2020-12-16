<template>
  <v-container>
    <v-list>
      <template v-for="(item, index) in similarSentences">
        <v-list-item :key="index" router :to="{name: 'Text', params: {slug: item.slug}}">
          <v-list-item-content>
            <v-list-item-title>{{ item.sentence }}</v-list-item-title>
            <v-list-item-subtitle>{{ item.distance }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>
  </v-container>
</template>

<script>
export default {
  name: 'Sentences',
  props: {
    similarSentences: {
      type: Array,
      required: true,
    },
  },
}
</script>
