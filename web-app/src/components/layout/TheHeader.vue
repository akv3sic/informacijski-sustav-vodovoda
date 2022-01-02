<template>
    <div>
      <v-app-bar
        color="blue darken-2"
        dark
        :class="{'px-16':$vuetify.breakpoint.mdAndUp}"
      >
          <v-spacer class="hidden-md-and-up"></v-spacer>
          <v-toolbar-title>
              <!--<v-img src="@/assets/img/logo.png" max-width="50px" />-->
              Vodovod X
          </v-toolbar-title>

          <v-spacer></v-spacer>

          <!-- Hidden on mobile -->
          <v-btn 
            outlined
            @click="$router.push({ path: '/prijava' })"
            class="hidden-sm-and-down"
          >
            PRIJAVA
          </v-btn>

          <v-btn 
            icon
            class="hidden-sm-and-down"
          >
            <v-icon>mdi-magnify</v-icon>
          </v-btn>
        <!-- Hidden on mobile END -->


        <!-- Mobile menu icon -->
        <v-btn 
            @click.stop="drawer = !drawer"
            text
            class="hidden-md-and-up"
        >
            <v-icon large right>mdi-menu</v-icon>
        </v-btn>
      </v-app-bar>

      <!-- Mobile menu -->
      <v-navigation-drawer
          v-model="drawer"
          absolute
          temporary
          right
      >
        <v-list 
            dense
            nav
        >
            <v-subheader class="my-4">
                  <img class="mx-auto" :src="require('@/assets/img/logo.png')" height="30"/>
            </v-subheader>
            <v-list-item-group>
                <v-list-item to="/prijava">
                  <v-list-item-icon>
                      <v-icon>mdi-login</v-icon>
                  </v-list-item-icon>
                  <v-list-item-title>Prijava</v-list-item-title>
                </v-list-item>
            </v-list-item-group>
        </v-list>
      </v-navigation-drawer>
    </div>
   
</template>

<script>
export default {
    name: "Header",
    data: () => ({
      drawer: false
    })
}
</script>