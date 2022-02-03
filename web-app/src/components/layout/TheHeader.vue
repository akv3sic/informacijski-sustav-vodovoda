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
            <a href="/" class="rm-text-decoration white--text">
              Vodovod X
            </a>
          </v-toolbar-title>

          <v-spacer></v-spacer>

          <!-- Hidden on mobile -->

          <v-toolbar-items class="hidden-sm-and-down">
              <v-list-item
                v-for="(item, index) in navigationItems"
                :key="index"
                :to="item.to"
                class="mx-2"
                >
                <v-list-item-title class="text-body font-weight-medium white-title">{{ item.title }}</v-list-item-title>
              </v-list-item>
          </v-toolbar-items>

          <v-btn 
            outlined
            @click="$router.push({ path: '/prijava' })"
            class="hidden-sm-and-down ml-2"
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
                 <v-list-item
                  v-for="(item, index) in navigationItems"
                  :key="index"
                  :to="item.to"
                  >
                  <v-list-item-icon>
                      <v-icon> {{ item.icon }} </v-icon>
                  </v-list-item-icon>
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item>

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
      drawer: false,
       navigationItems: [
                {title: 'Novosti', to:'/novosti', icon: 'mdi-newspaper-variant-outline'},
                {title: 'Prijava kvara', to:'/prijava-kvara', icon: 'mdi-alert'},
      ],
    })
}
</script>

<style>
.rm-text-decoration {
  text-decoration: none;
}
.white-title {
  color: white !important;
}
</style>