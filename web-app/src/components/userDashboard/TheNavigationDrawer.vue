<template>
    <div>
        <v-navigation-drawer 
            color="secondary"
            v-model="drawer"
            app
        >
        <v-list-item>
            <v-list-item-content>
                <v-row>
                    <v-col justify-center>
                    <router-link to="/" class="text-decoration-none  text-uppercase primary--text">
                        <span class="d-inline">Informacijski sustav</span><br>
                        <img class="mx-3" :src="require('@/assets/img/logo.png')" height="29"/>
                        <span class="ml-2 d-inline font-weight-bold">vodovoda X</span>
                    </router-link>
                    </v-col>
                </v-row>
            </v-list-item-content>
        </v-list-item>

              <v-select
              v-model="selectedContract"
              :items="contracts"
              :item-text="item => item.ulica + ' ' + item.kucni_broj"
              label="Odabir priključka"
              no-data-text="Nema priključaka"
              item-value="id"
              outlined
              class="px-4 pt-4"
              >
              </v-select>

            <v-list
                nav
                dense
            >
                 <v-list-item
                 v-for="item in navigationItems"
                 :key="item.title"
                 :to="item.to"
                 >
                    <v-list-item-icon>
                    <v-icon v-text="item.icon"></v-icon>
                    </v-list-item-icon>

                    <v-list-item-title v-text="item.title"></v-list-item-title>
                </v-list-item>

            </v-list>
            <!-- ide na dno -->
            <template v-slot:append>
              <div class="pa-2">
                <v-list-item
                    to="/podrska"
                    exact
                    >
                    <v-list-item-title>Podrška</v-list-item-title>
                </v-list-item>
              </div>
          </template>

        </v-navigation-drawer>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    name: 'UserNavigationDrawer',
    data: () => ({
      navigationItems: [
        {
          icon: 'mdi-card-account-details',
          title: 'Osobni podatci',
          to: '/moj-racun/osobni-podatci'
        },
        {
          icon: 'mdi-receipt',
          title: 'Računi',
          to: '/moj-racun/racuni'
        },
                {
          icon: 'mdi-water',
          title: 'Pregled potrošnje',
          to: '/moj-racun/pregled-potrosnje'
        },
        {
          icon: 'mdi-message-alert',
          title: 'Prijava kvara',
          to: '/moj-racun/prijava-kvara'
        },
        {
          icon: 'mdi-cog',
          title: 'Postavke',
          to: '/moj-racun/postavke'
        }
      ],
    }),
    created() {
        this.fetchContracts()
    },
    methods: {
      fetchContracts() {
          this.$store
              .dispatch('userDashboard/fetchContracts', null, {root: true})
      },
    },
    computed: {
      drawer: {
        get () {
          return this.$store.getters['userDashboard/drawer']
        },
        set (val) {
          this.$store.dispatch('userDashboard/setDrawer', val)
        },
      },
      ...mapGetters('userDashboard', ['contracts', 'isLoading']),

      selectedContract: {
        get () {
          return this.$store.getters['userDashboard/selectedContract']
        },
        set (val) {
          this.$store.dispatch('userDashboard/setSelectedContract', val)
        },
      },
    },
}
</script>