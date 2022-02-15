<template>
    <v-container class="">
        <h2 class="mb-2">Zahtjevi za novi priključak <span class="grey--text"> ({{requests.length}}) </span> </h2>
        <v-row class="mb-5">
            <v-col>
                <span class="accent--text"> Pregledajte zahtjeve za nove priključke i odobrite ih ili odbijte. </span>
            </v-col>
            <v-col>
                <v-btn class="accent px-5" to="prikljucci">
                    Pregled priključaka
                </v-btn>
            </v-col>
        </v-row>

        
        <!-- kartice s zahtjevima -->
        <v-card 
            v-for="request in requests"
            :key="request.idPrikljucka"
            class="my-8"
        >
            <v-row>
                <v-col>
                    <v-card-title> ID zahtjeva: {{ request.id }} </v-card-title>    
                    <v-card-text>
                        Podnositelj: {{ request.prikljucak.korisnik.username }} {{ request.prikljucak.korisnik.userlastname }}
                        <p class="text-caption"> {{ request.prikljucak.korisnik.ulica.ulica }} {{ request.prikljucak.korisnik.kucni_broj }} </p>
                    </v-card-text>
                </v-col>


                <v-col class="d-flex  align-center">
                    <v-card-text>
                        <b>Adresa priključka:</b>  <br> {{ request.prikljucak.ulica }} {{ request.prikljucak.kucni_broj }}, <br> {{ request.prikljucak.mjesto }}
                    </v-card-text>
                </v-col>

                <v-col class="d-flex align-center">

                        <v-btn 
                            class="ma-3 primary"
                        >
                            Vidi zahtjev
                        </v-btn>
                        
                </v-col>
            </v-row>


        </v-card>
        <!-- stranicenje -->
        <v-pagination
        :length="3"
        disabled
        ></v-pagination>
      
    </v-container>
</template>

<script>
import { mapGetters } from "vuex"

export default {
    name: "AdminRequestsOverview",
    data: () => ({

    }),
    mounted() {
        this.fetchRequests()
    },
    methods: {
        fetchRequests() {
            this.$store
                .dispatch('adminRequests/fetchRequests', null, {root: true})
        },
    },
    computed: {
        ...mapGetters('adminRequests', ['isLoading', 'requests'])
    },
    watch: {
    }
}
</script>

<style>
.filter-item {
    max-width: 240px;
    margin: 0px 12px;
}   
</style>