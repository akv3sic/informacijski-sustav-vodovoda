<template>
    <v-container class="pa-16 max-85">
        <h2 class="mb-2">Pregled potrošnje</h2>
        <v-row class="mb-5">
            <v-col>
                <span class="accent--text">Stanje brojila (pri zadnjem očitavanju): 107</span>
            </v-col>
        </v-row>
        
        <!--  grafički prikaz potrošnje -->
        <GraphicalConsuptionOverview 
            :labels="graphLabels"
            :values="graphValues"
        />

         <!-- kartice s potrošnjom za pojedini mjesec -->
        <v-card 
            v-for="stavka in potrosnjaPoMjesecima"
            :key="stavka.id"
            max-width="50vw"
            class="my-8 px-4"
        >
            <v-row>
                <v-col>
                    <v-card-title class="font-italic"> {{ stavka.mjesec }}/{{ stavka.godina}} </v-card-title>         
                    <v-card-text>
                        Datum očitavanja: {{ stavka.datumOcitavanja }}
                    </v-card-text>
                </v-col>
                <v-col>
                    <v-card-text> Prethodno stanje: {{ stavka.prethodnoStanje }} </v-card-text>         
                    <v-card-text> Novo stanje: {{ stavka.novoStanje }} </v-card-text>         
                </v-col>
                <v-col class="d-flex justify-center">
                    <v-card-actions>
                        <span class="pa-4 font-weight-medium">
                            {{ stavka.novoStanje - stavka.prethodnoStanje }}
                            m<sup>3</sup>
                        </span>
                        <v-icon large color="blue darken-3" v-if="stavka.status=='increasing'">mdi-arrow-up-bold</v-icon>
                        <v-icon large color="blue lighten-2" v-else>mdi-arrow-down-bold</v-icon>
                    </v-card-actions>
                    
                </v-col>
            </v-row>
        </v-card>

        
     
      
    </v-container>
</template>

<script>
import GraphicalConsuptionOverview from '@/components/userDashboard/GraphicalConsOverview.vue'

export default {
    name: "UserConsuptionOverview",
    components: { GraphicalConsuptionOverview },
    data: () => ({
         potrosnjaPoMjesecima: [
            { id: 732, mjesec: "01", godina: "2020", datumOcitavanja: "23. 1. 2022.", prethodnoStanje: "90", novoStanje: "107", status: "decreasing" },
            { id: 738, mjesec: "12", godina: "2020", datumOcitavanja: "23. 1. 2022.", prethodnoStanje: "90", novoStanje: "107", status: "increasing" },
            { id: 739, mjesec: "11", godina: "2020", datumOcitavanja: "23. 1. 2022.", prethodnoStanje: "90", novoStanje: "107", status: "increasing" },
            { id: 790, mjesec: "10", godina: "2020", datumOcitavanja: "23. 1. 2022.", prethodnoStanje: "90", novoStanje: "107", status: "increasing" }
        ],
        graphLabels: [
        '2.',
        '3.',
        '4.',
        '5.',
        '6.',
        '7.',
        '8.',
        '9.',
        '10.',
        '11.',
        '12.',
        '1.',
      ],
      graphValues: [
        0, 0, 0, 0, 0, 0, 0, 0, 15, 20, 25, 17
      ],
    }),
    methods: {

    }    
}
</script>

<style>
.max-85 {
    max-width: 85vw;
}
</style>