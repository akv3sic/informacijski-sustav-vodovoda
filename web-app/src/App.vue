<template>
<v-app>

  <!-- Sizes your content based upon application components -->
  <v-main>

    <!-- Provides the application the proper gutter -->
    <v-container 
      fluid 
      class="pa-0" 
      :class="{'fill-height':$route.name == 'NotFound' || $route.path == '/prijava' 
                || $route.path == '/resetiranje-lozinke'
                || $route.path == '/registracija'
                }"> 

      <!-- vue-router -->
      <router-view></router-view>
    </v-container>
  </v-main>

</v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>
