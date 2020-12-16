<template>
  <v-app>
    <v-app-bar app>
      <router-link
          router
          to="/"
          class="text-decoration-none text-uppercase white--text pl-5"
      >
        <span class="font-weight-light">Similar</span>
        <span>Sentences</span>
      </router-link>
    </v-app-bar>
    <v-main>
      <v-container>
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
};
</script>
