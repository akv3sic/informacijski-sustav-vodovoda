<template>
    <v-footer
        color="#fff"
        class="pt-7 pb-3"
    >
        <v-row class="px-16">
            <v-col>
                <h3>Pratite nas</h3>
                <a href="https://facebook.com" target="_blank" class="rm-text-decoration">
                    <v-icon class="ma-2" x-large>mdi-facebook</v-icon>
                </a>
                <a href="https://linkedin.com" target="_blank" class="rm-text-decoration">
                    <v-icon class="ma-2" x-large>mdi-linkedin</v-icon>
                </a>
            </v-col>
            <v-col>
                <!-- KORISNICI -->
                <h3>Korisnici</h3>
                <v-list-item
                    v-for="item in korisniciNavItems"
                    :key="item.id"
                    :to="item.link"
                    class="nav-item"
                >
                    {{ item.name }}
                </v-list-item>
            </v-col>
            <v-col>
                <!-- TVRTKA -->
                <h3>Tvrtka</h3>
                <v-list-item
                    v-for="item in tvrtkaNavItems"
                    :key="item.id"
                    :to="item.link"
                    class="nav-item"
                >
                    {{ item.name }}
                </v-list-item>
            </v-col>
            <v-col>
                <!-- VIŠE INFORMACIJA -->
                <h3>Više informacija</h3>
            <v-list-item
                    v-for="item in viseInformacijaNavItems"
                    :key="item.id"
                    :to="item.link"
                    class="nav-item"
                >
                    {{ item.name }}
                </v-list-item>
            </v-col>

            <v-col 
                cols="12"
                class="pt-7 pb-1 text-center"
            >
                &copy; {{ new Date().getFullYear() }} — <strong class="primary--text">Vodovod X</strong>
            </v-col>

            <v-col 
                cols="12"
                class="pt-1 text-center"
            >
                Zaštita privatnosti | Uvjeti korištenja
            </v-col>
        </v-row>
    </v-footer>
</template>

<script>
export default {
    name: "Footer",
    data: () => ({
        korisniciNavItems: [
            { id: 1, name: "Često postavljana pitanja", link: "/cesto-postavljana-pitanja" },
            { id: 2, name: "Moj račun", link: "" },
            { id: 3, name: "Sit dolor", link: "" }
        ],
        tvrtkaNavItems: [
            { id: 1, name: "Više o nama", link: "" },
            { id: 2, name: "Investitiori", link: "" },
            { id: 3, name: "Blog", link: "" }
        ],
        viseInformacijaNavItems: [
            { id: 1, name: "Lorem ipsum", link: "" },
            { id: 2, name: "Sit dolor", link: "" },
            { id: 3, name: "Excepteur sint", link: "" }
        ]
    })
}
</script>

<style scoped>
ul {
    list-style-type: none;
}
.nav-item {
    padding-left: 0 !important;
    color: grey !important;
}
.nav-item:hover {
    background-color: transparent !important;
}
</style>