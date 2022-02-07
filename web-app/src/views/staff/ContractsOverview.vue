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
                 v-model="filters.selectedPlace"
                :items="filters.statuses"
                filled
                label="Filtriraj po mjestu"
                ></v-select> 
            </span>
            <span class="filter-item" v-if="filters.selectedPlace != ''">
                <v-select
                v-model="filters.selectedStreet"
                :items="filters.statuses"
                filled
                label="Filtriraj po ulici"
                ></v-select> 
            </span>
            <span class="filter-item">
                <v-switch
                v-model="filters.withRequestsOnly"
                label="Samo nepopisani"
                ></v-switch>
            </span>
        </div>
        
        <!-- kartice s računima -->
        <v-card 
            v-for="prikljucak in filteredprikljucci"
            :key="prikljucak.id"
            class="my-8"
        >
            <v-row>
                <v-col>
                    <v-card-title> Priključak ID: {{ prikljucak.id }} </v-card-title>         
                    <v-card-text>
                        Vlasnik: {{ prikljucak.ime }} {{ prikljucak.prezime }}
                    </v-card-text>
                </v-col>


                <v-col class="d-flex  align-end">     
                    <v-card-text>
                        Mjesto: {{ prikljucak.mjesto }}
                        <br>
                        Adresa: {{ prikljucak.adresa }}
                    </v-card-text>
                </v-col>

                <v-col>
                    <v-card-text>
                        Stanje brojila: {{ prikljucak.stanjeBrojila }}
                        <br>
                        <v-btn class="mt-3 teal lighten-4" :disabled="prikljucak.status == 'Popisano'"> Upiši stanje </v-btn>
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
export default {
    name: "StaffContractsOverview",
    data: () => ({
        prikljucci: [
            { id: 732, ime: "Jure", prezime: "Jurić", mjesto: "Mjesto", adresa: "Street 22",  status: "Nepopisano", stanjeBrojila: "523" },
            { id: 733, ime: "Jure", prezime: "Jurić", mjesto: "Mjesto", adresa: "Street 22",  status: "Nepopisano", stanjeBrojila: "523" },
            { id: 734, ime: "Jure", prezime: "Jurić", mjesto: "Mjesto", adresa: "Street 22",  status: "Popisano", stanjeBrojila: "523" },
            { id: 738, ime: "Jure", prezime: "Jurić", mjesto: "Mjesto", adresa: "Street 22",  status: "Popisano", stanjeBrojila: "523" },
        ],
        filters: {
            selectedPlace: "dd",
            selectedStreet: "",
            statuses: ['Sve', 'Pristiglo', 'Plaćeno', 'Zakašnjelo'],
            withRequestsOnly: false    
        }
    }),
    methods: {
      
    } ,
    computed: {
        // by status
        filteredprikljucci: function() {
            return this.prikljucci.filter((prikljucak) => {
                return prikljucak.status.match(this.filters.selectedStatus) || this.filters.selectedStatus == "Sve"
            });
        },
    }
}
</script>

<style>
.filter-item {
    max-width: 240px;
    margin: 0px 12px;
}   
</style>