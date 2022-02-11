<template>
    <div>
        <Navbar />
        <NavigationDrawer />
        <v-container fluid class="pa-0" :class="{'px-7':$vuetify.breakpoint.mdAndUp}">
            <!-- Ovdje se injektiraju pogledi -->
          <router-view></router-view>
       </v-container>
    </div>
</template>

<script>
import Navbar from "@/components/userDashboard/TheNavbar"
import NavigationDrawer from "@/components/userDashboard/TheNavigationDrawer"

export default {
    name: "userHome",
    components: { Navbar, NavigationDrawer },
}
</script>