<template>
    <v-container class="pa-16 max-85">
        <h2 class="mb-2">Postavke</h2>

        <v-row class="mb-5 mt-2">
            <!-- tamna tema -->
            <v-col>
            <v-switch
                v-model="$vuetify.theme.dark"
                inset
                label="Tamna tema"
                persistent-hint
            ></v-switch>
            </v-col>
        </v-row>

      
    </v-container>
</template>

<script>
export default {
    name: "UserSettings",
    
}
</script>

<style>
.max-85 {
    max-width: 85vw;
}
</style>