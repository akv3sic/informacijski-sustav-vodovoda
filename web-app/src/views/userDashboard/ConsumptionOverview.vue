<template>
    <v-container class="">
        <h2 class="mb-2">Pregled potrošnje</h2>
        <v-row class="mb-5">
            <v-col>
                <span class="accent--text" v-if="!isLoading">Stanje brojila (pri zadnjem očitavanju): 
                    {{  Math.round(consuption[0].potrosnja) + consuption[0].prethodno_stanje  }}
                </span>
            </v-col>
        </v-row>
        
        <!--  grafički prikaz potrošnje -->
        <GraphicalConsuptionOverview 
            :labels="graphLabels"
            :values="graphValues"
        />

         <!-- kartice s potrošnjom za pojedini mjesec -->
        <v-card 
            v-for="(stavka, index) in consuption"
            :key="index"
            class="my-8 px-4"
        >
            <v-row>
                <v-col>
                    <v-card-title class="font-italic"> {{ stavka.mjesec }} index {{index}}</v-card-title>         
                    <v-card-text>
                        Datum očitavanja: {{ stavka.datum_ocitavanja.replaceAll("-", ".") }}
                    </v-card-text>
                </v-col>
                <v-col>
                    <v-card-text> Prethodno stanje: {{ stavka.prethodno_stanje }} </v-card-text>         
                    <v-card-text> Novo stanje: {{ stavka.prethodno_stanje +  Math.round(stavka.potrosnja) }} </v-card-text>         
                </v-col>
                <v-col class="d-flex justify-center">
                    <v-card-actions>
                        <span class="pa-4 font-weight-medium">
                            {{ Math.round(stavka.potrosnja) }}
                            m<sup>3</sup>
                        </span>
                        <v-icon large color="blue darken-3" v-if="stavka">mdi-arrow-up-bold</v-icon>
                        <v-icon large color="blue lighten-2" v-else>mdi-arrow-down-bold</v-icon>
                    </v-card-actions>
                    
                </v-col>
            </v-row>
        </v-card>

        
     
      
    </v-container>
</template>

<script>
import GraphicalConsuptionOverview from '@/components/userDashboard/GraphicalConsOverview.vue'
import { mapGetters } from "vuex"

export default {
    name: "UserConsuptionOverview",
    components: { GraphicalConsuptionOverview },
    data: () => ({
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
    mounted(){
        this.fetchConsuption()
    },
    methods: {
        fetchConsuption() {
          this.$store
              .dispatch('userConsuptionOverview/fetchConsuption', this.selectedContract, {root: true})
      },
    },
    computed: {
        ...mapGetters('userDashboard', ['selectedContract']),
        ...mapGetters('userConsuptionOverview', ['consuption', 'isLoading']),
    },
    watch: {
        selectedContract(newValue){
            console.log("odabrani prikljucak promijenjen " + newValue)
            this.fetchConsuption()
        }
    }    
}
</script>

<style>
.max-85 {
    max-width: 85vw;
}
</style>