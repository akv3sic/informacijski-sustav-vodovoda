<template>
    <v-app-bar
      color="blue darken-2"
      class="px-10"
      dark
    >

        <v-toolbar-title>
            <!--<v-img src="@/assets/img/logo.png" max-width="50px" />-->
            Vodovod X
        </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn outlined>
        PRIJAVA
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

    </v-app-bar>
</template>

<script>
export default {
    name: "Header"
}
</script>