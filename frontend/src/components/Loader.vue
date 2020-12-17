<template>
  <div
      class="d-flex justify-center"
  >
    <v-progress-circular
        :size="70"
        :width="7"
        color="purple"
        indeterminate
    />
  </div>
</template>

<script>
export default {
  name: 'Loader',
}
</script>
