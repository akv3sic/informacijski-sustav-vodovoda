<template>
    <div>
        <Navbar />
        <v-container fluid class="pa-0">
            <!-- Ovdje se injektiraju pogledi -->
          <router-view></router-view>
       </v-container>
    </div>
</template>

<script>
import Navbar from "@/components/staff/TheNavbar"

export default {
    name: "adminHome",
    components: { Navbar },
}
</script>