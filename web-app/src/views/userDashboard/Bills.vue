<template>
    <v-container class="pa-16 max-85">
        <h2 class="mb-2">Računi</h2>
        <v-row class="mb-5">
            <v-col>
                <span class="accent--text">Pregledajte stare račune ili platite račun.</span>
            </v-col>
            <v-col>
                <v-btn class="primary" to="pregled-potrosnje">Pregled potrošnje</v-btn>
            </v-col>
        </v-row>

        <!-- filteri -->
        <div class="d-flex filters-section">
            <span class="filter-item">
                 <v-select
                 v-model="filters.selectedStatus"
                :items="filters.statuses"
                filled
                label="Status računa"
                ></v-select> 
            </span>
        </div>
        
        <!-- kartice s računima -->
        <v-card 
            v-for="bill in filteredBills"
            :key="bill.id"
            max-width="50vw"
            class="my-8"
        >
            <v-row>
                <v-col>
                    <v-card-title> Račun za {{ bill.mjesec }}  </v-card-title>         
                    <v-card-text>
                        Datum dospijeća: {{ bill.datum_dospijeca }}
                        <br>
                        Datum plaćanja: {{ bill.datum_placanja }}
                    </v-card-text>
                </v-col>


                <v-col class="d-flex  align-end">     
                    <v-card-text>
                        Ukupno za platiti:
                        <br>
                        {{ bill.ukupno }} KM
                    </v-card-text>
                </v-col>

                <v-col>
                    <v-card-text>
                        Račun br.: {{ bill.id }}
                        <br>
                        <v-btn class="mt-3 teal lighten-4" :disabled="bill.placeno == true"> Idi na plaćanje </v-btn>
                    </v-card-text>
                </v-col>

                <v-col class="d-flex justify-center">
                    <v-card-actions>
                    <v-chip
                        :class="{
                                    'rotate90': $vuetify.breakpoint.lgAndUp,
                                    'green': bill.placeno == true,
                                    'yellow lighten-3': bill.placeno == false,
                                }"
                        class="status-chip mx-3"
                    >
                        {{ bill.placeno ? 'Plaćeno' : 'Neplaćeno' }} 
                    </v-chip> 
                    </v-card-actions>
                </v-col>
            </v-row>
        </v-card>


     
      
    </v-container>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    name: "MyBills",
    data: () => ({
        billsMockUp: [
            { id: 732, mjesec: "01", godina: "2020", dospijece: "20. 1. 2022.", placanje: "23. 1. 2022.", ukupno: "18,16", status: "Neplaćeno" },
            { id: 738, mjesec: "12", godina: "2020", dospijece: "20. 1. 2022.", placanje: "23. 1. 2022.", ukupno: "42,90", status: "Plaćeno" },
            { id: 835, mjesec: "11", godina: "2020", dospijece: "20. 1. 2022.", placanje: "23. 1. 2022.", ukupno: "19,16", status: "Neplaćeno" },
            { id: 890, mjesec: "10", godina: "2020", dospijece: "20. 1. 2022.", placanje: "23. 1. 2022.", ukupno: "18,16", status: "Plaćeno" }
        ],
        filters: {
            selectedStatus: "Svi",
            statuses: ['Svi', 'Plaćeno', 'Neplaćeno'],
        }
    }),
    mounted() {
        this.fetchBills()
    },
    methods: {
      fetchBills() {
          this.$store
              .dispatch('userBills/fetchBills', this.selectedContract, {root: true})
      },
    },
    computed: {
        // by status
        filteredBills: function() {
            if (this.filters.selectedStatus == 'Plaćeno') {
                return this.bills.filter((bill) => {
                    return bill.placeno == true
                }); 
            }
            else if(this.filters.selectedStatus == 'Neplaćeno') {
                return this.bills.filter((bill) => {
                    return bill.placeno == false
                }); 
            }
            else {
                return this.bills
            } 
        },
        ...mapGetters('userDashboard', ['selectedContract']),
        ...mapGetters('userBills', ['bills']),
    },
    watch: {
        selectedContract(newValue){
            console.log("odabrani prikljucak promijenjen " + newValue)
            this.fetchBills()
        }
    }
}
</script>

<style>
.max-85 {
    max-width: 85vw;
}
.filters-section {
    max-width: 50vw;
}
.filter-item {
    max-width: 240px;
    margin: 0px 12px;
}   
</style>