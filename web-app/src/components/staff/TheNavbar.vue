<template>
    <div>
        <v-app-bar
            color="blue darken-2"
            dark
            app
            flat
        >
            <v-spacer></v-spacer>
            <v-toolbar-title>Popisivanje potrošnje</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn icon class="hidden-sm-and-down">
                <v-icon>mdi-bell-outline</v-icon>
            </v-btn>

            <v-menu offset-y left>
                <template v-slot:activator="{ on, attrs }">    
                    <v-btn icon v-bind="attrs" v-on="on">
                            <v-icon class="hidden-sm-and-down">mdi-account-circle</v-icon>
                    </v-btn>
                </template>
                    <v-list
                        dense
                    >
                    <v-list-item
                    v-for="(item, index) in accountMenuItems"
                    :key="index"
                    @click="handleAccountMenuItemClick(item.action)"
                    :to="item.to"
                    >
                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>

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

                    <v-list-item @click="logOut">
                    <v-list-item-icon>
                        <v-icon>mdi-login</v-icon>
                    </v-list-item-icon>
                    <v-list-item-title>Odjava</v-list-item-title>
                    </v-list-item>
                </v-list-item-group>
            </v-list>
        </v-navigation-drawer>
    </div>
</template>

<script>

export default {
    name: 'Navbar',
    data: () => ({
       accountMenuItems: [
            { title: 'Moj račun', action: '', to: 'moj-racun'},  
            { title: 'Prijava kvara', action: '', to: 'prijava-kvara'},  
            { title: 'Odjava', action: 'logOut', to: '#'},  
        ],
        drawer: false,
        navigationItems: [
            {title: 'Moj račun', to:'moj-racun', icon: 'mdi-account'},
            {title: 'Prijava kvara', to:'/prijava-kvara', icon: 'mdi-alert'},
      ],
    }),
     methods: {
        handleAccountMenuItemClick(action) {
             switch(action) {
             case 'logOut':
                this.$store
                    .dispatch('auth/logOut', { root: true })
                this.$router.push({path: '/'})
                break;
                }
            },
        logOut() {
          this.$store
          .dispatch('auth/logOut', { root: true })
      },
    },
}
</script>