<template>
    <div>
        <Navbar />
        <v-container fluid class="pa-0">
            <!-- Ovdje se injektiraju pogledi -->
          <router-view></router-view>
       </v-container>
       <BottomNavigation />
    </div>
</template>

<script>
import Navbar from "@/components/staff/TheNavbar"
import BottomNavigation from "@/components/staff/TheBottomNavigation"

export default {
    name: "adminHome",
    components: { Navbar, BottomNavigation },
}
</script>