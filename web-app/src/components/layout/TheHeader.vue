<template>
    <div>
      <v-app-bar
        color="blue darken-2"
        dark
        :class="{'pl-16':$vuetify.breakpoint.mdAndUp}"
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

          <!--
            IF AUTH
          -->
        <v-menu offset-y v-if="isLoggedIn">
          <template v-slot:activator="{ on, attrs }">
            <!-- avatar -->
            <v-avatar
              @click="fetchUserData"
              color="accent"
              size="40"
              v-bind="attrs"
              v-on="on"
            >
            {{ avatarText }}
            </v-avatar>

          </template>

          <v-card>
            <v-list>
              <v-list-item>
                <v-list-item-avatar>
                  <v-avatar
                    color="accent"
                    size="40"
                  >
                  {{ avatarText }}
                  </v-avatar>
                </v-list-item-avatar>

                <v-list-item-content>
                  <v-list-item-title>{{ user.username }} {{ user.userlastname }}</v-list-item-title>
                  <v-list-item-subtitle>{{ user.email }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>

            <v-divider></v-divider>

            <v-list>
              <v-list-item to="/moj-racun">
                  <v-icon class="mx-2">
                    mdi-account
                  </v-icon>
                <v-list-item-title>Moj račun</v-list-item-title>
              </v-list-item>
              <v-list-item to="/moj-racun/postavke">
                  <v-icon class="mx-2">
                    mdi-cog
                  </v-icon>
                <v-list-item-title>Postavke</v-list-item-title>
              </v-list-item>
            </v-list>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                text
                @click="logOut()"
              >
                Odjava
              </v-btn>
            </v-card-actions>
          </v-card>

        </v-menu>
          <!--
            IF AUTH END
          -->

          <v-btn 
            outlined
            @click="$router.push({ path: '/prijava' })"
            class="hidden-sm-and-down ml-2"
            v-else
          >
            PRIJAVA
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
import { mapGetters } from "vuex"

export default {
    name: "Header",
    data: () => ({
      drawer: false,
      navigationItems: [
                {title: 'Novosti', to:'/novosti', icon: 'mdi-newspaper-variant-outline'},
                {title: 'Prijava kvara', to:'/prijava-kvara', icon: 'mdi-alert'},
      ],
}),

    computed: {
      ...mapGetters('auth', ['isLoggedIn', 'avatarText']),
      ...mapGetters('userAccountDetails', ['isLoading', 'user'])
    },

    methods: {
      logOut() {
          this.$store
          .dispatch('auth/logOut', { root: true })
      },
      fetchUserData() {
            this.$store
                .dispatch('userAccountDetails/fetchUserDetails', null, {root: true})
        },
    }
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