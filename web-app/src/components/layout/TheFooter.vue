<template>
    <v-footer
        color="blue darken-2"
        dark
        class="pt-7 pb-3"
    >
        <v-row class="px-16">
            <v-col>
                <h3>Pratite nas</h3>
                <a href="https://facebook.com" target="_blank">
                    <v-icon class="ma-2" x-large>mdi-facebook</v-icon>
                </a>
                <a href="https://linkedin.com" target="_blank">
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
                class="pt-7 text-center"
            >
                &copy; {{ new Date().getFullYear() }} — <strong>Vodovod X</strong>
            </v-col>
        </v-row>
    </v-footer>
</template>

<script>
export default {
    name: "Footer",
    data: () => ({
        korisniciNavItems: [
            { id: 1, name: "Često postavljana pitanja", link: "" },
            { id: 2, name: "Moj račun", link: "" },
            { id: 3, name: "Prijava kvara", link: "" }
        ],
        tvrtkaNavItems: [
            { id: 1, name: "O nama", link: "" },
            { id: 2, name: "Javne nabavke", link: "" },
            { id: 3, name: "Lorem ipsum", link: "" }
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
    color: white !important;
}
.nav-item:hover {
    background-color: transparent !important;
}
</style>