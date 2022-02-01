<template>
    <v-container class="pa-16 max-70">
        <h2 class="mb-2">Pregled potrošnje</h2>
        <v-row class="mb-5">
            <v-col>
                <span>Zadnje očitano stanje brojila: 107</span>
            </v-col>
        </v-row>
        

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
export default {
    name: "UserConsuptionOverview",
    data: () => ({
         potrosnjaPoMjesecima: [
            { id: 732, mjesec: "01", godina: "2020", datumOcitavanja: "23. 1. 2022.", prethodnoStanje: "90", novoStanje: "107", status: "decreasing" },
            { id: 738, mjesec: "12", godina: "2020", datumOcitavanja: "23. 1. 2022.", prethodnoStanje: "90", novoStanje: "107", status: "increasing" },
            { id: 739, mjesec: "11", godina: "2020", datumOcitavanja: "23. 1. 2022.", prethodnoStanje: "90", novoStanje: "107", status: "increasing" },
            { id: 790, mjesec: "10", godina: "2020", datumOcitavanja: "23. 1. 2022.", prethodnoStanje: "90", novoStanje: "107", status: "increasing" }
        ]
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