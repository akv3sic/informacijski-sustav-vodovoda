<template>
    <v-container class="">
        <h2 class="mb-2">Pregled priključaka</h2>
        <v-row class="mb-5">
            <v-col>
                <span class="accent--text"> Prikazani su aktivni priključci u vodovodnoj mreži. </span>
            </v-col>
            <v-col>
                <v-btn class="accent px-5" to="zahtjevi-za-novi-prikljucak">
                    Novi zahtjevi
                    <v-badge color="green" :content="noOfNewRequests" class="ma-1"></v-badge>
                </v-btn>
            </v-col>
        </v-row>

        <!-- filteri -->
        <div class="d-flex filters-section">
            <span class="filter-item">
                 <v-select
                 v-model="selectedPlace"
                :items="places"
                item-text="mjesto"
                filled
                label="Filtriraj po mjestu"
                ></v-select> 
            </span>

            <!-- Prikazuje se samo ako ima odabranih priključaka -->
            <span class="filter-item" v-if="selectedPlace">
                <v-select
                v-model="selectedStreet"
                :items="streets"
                item-text="ulica"
                filled
                label="Filtriraj po ulici"
                ></v-select> 
            </span>
        </div>
        
        <!-- kartice s računima -->
        <v-card 
            v-for="prikljucak in contracts"
            :key="prikljucak.idPrikljucka"
            class="my-8"
        >
            <v-row>
                <v-col>
                    <v-card-title> Priključak ID: {{ prikljucak.idPrikljucka }} </v-card-title>         
                    <v-card-text>
                        Vlasnik: {{ prikljucak.username }} {{ prikljucak.userlastname }}
                    </v-card-text>
                </v-col>


                <v-col class="d-flex  align-end">     
                    <v-card-text>
                        Mjesto: {{ prikljucak.mjesto }}
                        <br>
                        Adresa: {{ prikljucak.ulica }} {{ prikljucak.kucni_broj }}
                    </v-card-text>
                </v-col>

                <v-col>
                    <v-card-text>
                        Stanje brojila: {{ prikljucak.stanje_brojila }}
                        <br>

                        <v-btn 
                        class="mt-3 teal lighten-4"
                        :disabled="true"
                        >
                        Detalji priključka 
                        </v-btn>
                        
                    </v-card-text>
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
    name: "AdminContractsOverview",
    data: () => ({
        // filters
        selectedPlace: null,
        selectedStreet: null,
    }),
    mounted() {
        this.fetchPlaces()
        this.fetchContracts()
    },
    methods: {
        fetchPlaces() {
            this.$store
                .dispatch('placesAndStreets/fetchPlaces', null, {root: true})
        },
        
        // fetch contracts and filter by place and street (optionally)
        fetchContracts(place, street) {
            this.$store
                .dispatch('staffContracts/fetchContracts', { place: place, street: street }, {root: true})
        },
        fetchStreets(place) {
            this.$store
                .dispatch('placesAndStreets/fetchStreets', place, {root: true})
        },

    },
    computed: {

        ...mapGetters('placesAndStreets', ['isLoading', 'places', 'streets']),
        ...mapGetters('staffContracts', ['isLoading', 'contracts', 'showSuccessAlert', 'noOfNewRequests'])
    },
    watch: {
        selectedPlace(newValue) {
            console.log("mjesto promijenjeno: " + newValue)
            this.fetchStreets(newValue)
            this.fetchContracts(newValue, null)
        },
        selectedStreet(newValue) {
            console.log("ulica promijenjena: " + newValue)
            this.fetchContracts(null, newValue)
        }
    }
}
</script>

<style>
.filter-item {
    max-width: 240px;
    margin: 0px 12px;
}   
</style>