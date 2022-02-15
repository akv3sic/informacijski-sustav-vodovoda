<template>
    <v-container v-if="!isLoading">
        <v-row class="mb-5">
            <v-col>
                <h2 class="mb-2">Zahtjev za novi priključak br. {{ request.id }} </h2>
            </v-col>
            <v-col>
                <v-btn class="accent px-5" to="/admin/zahtjevi-za-novi-prikljucak">
                    Svi zahtjevi
                </v-btn>
            </v-col>
        </v-row>

        <!-- DETALJI ZAHTJEVA -->

        <v-card
            class="my-4"
            outlined
        >
            <v-card-title>Podatci o priključku</v-card-title>
            <v-card-text>
                <v-list-item>ID: {{ request.prikljucak.id }}</v-list-item>
                <v-list-item>Mjesto: {{ request.prikljucak.mjesto }}</v-list-item>
                <v-list-item>Adresa: {{ request.prikljucak.ulica }} {{ request.prikljucak.kucni_broj }}</v-list-item>
            </v-card-text>
        </v-card>

        <v-card
            class="my-4"
            outlined
        >
            <v-card-title>Podnositelj</v-card-title>
            <v-card-text>
                <v-list-item>
                    <v-list-item-icon>
                        <v-icon>mdi-account</v-icon>
                    </v-list-item-icon>
                    <v-list-item-subtitle> {{ request.prikljucak.korisnik.username }} {{ request.prikljucak.korisnik.userlastname }} </v-list-item-subtitle>
                </v-list-item>
                <v-list-item>
                    <v-list-item-icon>
                        <v-icon>mdi-email</v-icon>
                    </v-list-item-icon>
                    <v-list-item-subtitle> {{ request.prikljucak.korisnik.email }} </v-list-item-subtitle>
                </v-list-item>
                <v-list-item>
                    <v-list-item-icon>
                        <v-icon>mdi-phone</v-icon>
                    </v-list-item-icon>
                    <v-list-item-subtitle> {{ request.prikljucak.korisnik.telefon }} </v-list-item-subtitle>
                </v-list-item>
                <v-list-item>
                    <v-list-item-icon>
                        <v-icon>mdi-home</v-icon>
                    </v-list-item-icon>
                    <v-list-item-subtitle> {{ request.prikljucak.korisnik.ulica.ulica }} {{ request.prikljucak.korisnik.kucni_broj }} </v-list-item-subtitle>
                </v-list-item>
            </v-card-text>
        </v-card>

        <v-card
            class="my-4"
            outlined
        >
            <v-card-title>Priloženi dokumenti</v-card-title>
            <v-card-text>   
                <v-list-item>
                    Zahtjev i uplatnica:
                    <v-btn text small class="primary--text mx-2" @click="openDocument(request.zahtjev)"><v-icon>mdi-eye</v-icon></v-btn>
                </v-list-item>
                <v-list-item>
                    Katastarski plan:
                    <v-btn text small class="primary--text mx-2" @click="openDocument(request.katastarski_plan)"><v-icon>mdi-eye</v-icon></v-btn>
                </v-list-item>
                <v-list-item>
                    ZK izvadak:
                    <v-btn text small class="primary--text mx-2" @click="openDocument(request.zk_izvadak)"><v-icon>mdi-eye</v-icon></v-btn>
                </v-list-item>
            </v-card-text>
        </v-card>


        <!-- AKCIJE -->
        <v-row class="mt-5">
            <v-col>
                <span class="mb-2 accent-text"> Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sequi facilis molestias sunt vel quae commodi. </span>
            </v-col>
            <v-col>
                <v-btn class="green px-5" dark @click="approveRequest(request.id)">
                    Odobri zahtjev
                </v-btn>
            </v-col>
        </v-row>

    </v-container>
</template>

<script>
import store from "@/store";
import { mapGetters } from 'vuex'

export default {
    name: "RequestDetails",
    data: () => ({
     
    }),
    beforeRouteEnter(to, from, next) {
      store.dispatch('adminRequests/fetchRequest', to.params.id, {root: true})
      next()
    },
    methods: {
        openDocument(path) {
            const url = process.env.VUE_APP_BASE_URL + path.slice(1)
            console.log(url)
            window.open(url)
        },
        approveRequest(id) {
            console.log("approved: " + id)
            this.$store.dispatch('adminRequests/approveRequest', id, {root: true})
        }
    },
    computed: {
        ...mapGetters('adminRequests', ['request', 'isLoading'])
    }
}
</script>

<style scoped>

</style>