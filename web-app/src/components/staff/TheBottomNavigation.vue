<template>
    <v-bottom-navigation app>
        <v-btn 
            v-for="item in items"
            :key="item.id"
            :to="item.to"
        >
        <span> {{ item.text }} </span>

        <v-icon> {{ item.icon }} </v-icon>
        </v-btn>
    </v-bottom-navigation>
</template>

<script>

export default {
    name: 'BottomNavigation',
    data: () => ({
        items: [
                { id:1,  text: "Priključci", to: "pregled-prikljucaka", icon: "mdi-water-pump" },
                { id:2,  text: "Moji podatci", to: "osobni-podatci", icon: "mdi-account" },
                { id:3,  text: "Prijava kvara", to: "prijava-kvara", icon: "mdi-message-alert" },
            ]
    }),
}
</script>