<template>
    <v-container class="">
        <h2 class="mb-2">Pregled priključaka</h2>
        <v-row class="mb-5">
            <v-col>
                <span class="accent--text">Upišite novo stanje brojila za pojedini priključak.</span>
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

            <span class="filter-item">
                <v-switch
                v-model="samoNepopisani"
                label="Samo nepopisani"
                ></v-switch>
            </span>
        </div>
        
        <!-- kartice s računima -->
        <v-card 
            v-for="prikljucak in filteredPrikljucci"
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
                        :disabled="prikljucak.popisan == true"
                        @click="openDialog(prikljucak)"
                        >
                        Upiši stanje 
                        </v-btn>
                        
                    </v-card-text>
                </v-col>
            </v-row>

            <!--
                UPIS NOVOG STANJA BROJILA
            -->

            <v-dialog
            v-model="dialog"
            max-width="600px"
            :retain-focus="false"
            v-if="clickedContract"
            >

            <v-card>
                <v-card-title>
                <span class="text-h5">Upis novog stanja brojila</span>
                </v-card-title>
                <v-card-text>
                <v-container>
                    <v-row>
                    <v-col
                        cols="12"
                        sm="6"
                        md="7"
                    >
                        <p>Vlasnik: {{ clickedContract.username }} {{ clickedContract.userlastname }}</p>
                        <p>Adresa: {{ clickedContract.ulica }} {{ clickedContract.kucni_broj}}</p>
                    </v-col>
                    <v-col
                        cols="12"
                        sm="6"
                        md="4"
                    >
                        <v-text-field
                        label="Stanje brojila"
                        required
                        v-model="clickedContract.stanje_brojila"
                        ></v-text-field>
                    </v-col>
                    </v-row>
                </v-container>

                <v-alert type="success" v-if="showSuccessAlert">Stanje uspješno spremljeno.</v-alert>

                </v-card-text>
                <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                    color="accent"
                    text
                    @click="dialog = false"
                >
                    Natrag
                </v-btn>
                <v-btn
                    color="primary"
                    text
                    @click="saveNewWaterMeterEntry(clickedContract.idPrikljucka, clickedContract.stanje_brojila)"
                >
                    Spremi
                </v-btn>
                </v-card-actions>
            </v-card>
            </v-dialog>

            <!--
                UPIS NOVOG STANJA BROJILA KRAJ
            -->

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
    name: "StaffContractsOverview",
    data: () => ({
        /*prikljucci: [
            { id: 732, ime: "Jure", prezime: "Jurić", mjesto: "Mjesto", adresa: "Street 22",  status: "Nepopisano", stanjeBrojila: "523" },
            { id: 733, ime: "Jure", prezime: "Jurić", mjesto: "Mjesto", adresa: "Street 22",  status: "Nepopisano", stanjeBrojila: "523" },
            { id: 734, ime: "Jure", prezime: "Jurić", mjesto: "Mjesto", adresa: "Street 22",  status: "Popisano", stanjeBrojila: "523" },
            { id: 738, ime: "Jure", prezime: "Jurić", mjesto: "Mjesto", adresa: "Street 22",  status: "Popisano", stanjeBrojila: "523" },
        ],*/

        // filters
        samoNepopisani: false, 
        selectedPlace: null,
        selectedStreet: null,

        // dialog za upis novog stanja
        dialog: false,
        clickedContract: null
    }),
    mounted() {
        this.fetchPlaces()
        this.fetchContracts()
    },
    methods: {
        fetchPlaces() {
            this.$store
                .dispatch('staffPlacesAndStreets/fetchPlaces', null, {root: true})
        },
        
        // fetch contracts and filter by place and street (optionally)
        fetchContracts(place, street) {
            this.$store
                .dispatch('staffContracts/fetchContracts', { place: place, street: street }, {root: true})
        },
        fetchStreets(place) {
            this.$store
                .dispatch('staffPlacesAndStreets/fetchStreets', place, {root: true})
        },

        // otvara dijalog za upis novog stanja
        openDialog(prikljucak) {
            console.log("kliknuti prikljucak :" + JSON.stringify(prikljucak))
            this.clickedContract = prikljucak
            this.dialog = true
        },
        refreshContracts() {
            if(this.selectedStreet) {
                this.fetchContracts(null, this.selectedStreet)
            }
            else if(this.selectedPlace) {
                this.fetchContracts(this.selectedPlace, null)
            }
            else {
                this.fetchContracts()
            }
        },
        saveNewWaterMeterEntry(idPrikljucka, stanjeBrojila) {
            this.$store
                .dispatch('staffContracts/postNewEntry', { idPrikljucka, stanjeBrojila }, {root: true})
            setTimeout(function() {
                this.refreshContracts();
            }.bind(this), 2000);
        }
    },
    computed: {
        // filtrira samo nepopisane priključke (na klijentskoj strani!)
        filteredPrikljucci: function() {
            return this.contracts.filter((contract) => {
                if(this.samoNepopisani) {
                    return contract.popisan == false
                }
                else {
                    return contract
                }
            });
        },
        ...mapGetters('staffPlacesAndStreets', ['isLoading', 'places', 'streets']),
        ...mapGetters('staffContracts', ['isLoading', 'contracts', 'showSuccessAlert'])
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