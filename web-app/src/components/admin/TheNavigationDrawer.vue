<template>
    <div>
        <v-navigation-drawer 
            color="light-blue lighten-5"
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

        <v-divider></v-divider>

            <v-list
                nav
                dense
            >
                <v-list-item
                to="/admin"
                exact
                >
                    <v-list-item-icon>
                    <v-icon>mdi-view-dashboard</v-icon>
                    </v-list-item-icon>

                    <v-list-item-title>Izvještaj</v-list-item-title>
                </v-list-item>
                <v-list-group
                    v-for="item in navigationItemsMulti"
                    :key="item.title"
                    v-model="item.active"
                    :prepend-icon="item.icon"
                    no-action
                >
                    <template v-slot:activator>
                    <v-list-item-content>
                        <v-list-item-title v-text="item.title"></v-list-item-title>
                    </v-list-item-content>
                    </template>

                    <v-list-item
                    v-for="child in item.items"
                    :key="child.title"
                    :to="child.to"
                    >
                    <v-list-item-content>
                        <v-list-item-title v-text="child.title"></v-list-item-title>
                    </v-list-item-content>
                    </v-list-item>
                </v-list-group>

                 <v-list-item
                 v-for="item in navigationItemsSingle"
                 :key="item.title"
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
                    to="admin/podrska"
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

export default {
    name: 'NavigationDrawer',
    data: () => ({
        navigationItemsMulti: [
        {
          icon: 'mdi-package-variant-closed',
          items: [
            { title: 'Pregled korisnika', to: '/admin/svi-korisnici'},
            { title: 'Dodaj novog', to: '/admin/korisnici-dodaj-novog' },
          ],
          title: 'Korisnici',
        },
        {
          icon: 'mdi-account-supervisor',
          items: [{ title: 'Pregled' }, {title: 'Dodaj novog djelatnika'}],
          title: 'Osoblje',
        }
      ],
      navigationItemsSingle: [
        {
          icon: 'mdi-water-pump',
          title: 'Priključci',
        },
        {
          icon: 'mdi-label',
          title: 'Kategorije potrošnje',
        },
                {
          icon: 'mdi-message-alert',
          title: 'Kvarovi',
        },
        {
          icon: 'mdi-cog',
          title: 'Postavke',
        }
      ]
    }),
    computed: {
      drawer: {
        get () {
          return this.$store.getters['admin/drawer']
        },
        set (val) {
          this.$store.dispatch('admin/setDrawer', val)
        },
      },
    },
}
</script>