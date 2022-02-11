<template>
    <v-container>
        <v-row>
            <v-col>
                <span class="text-h5">Kategorije potrošnje</span>
                <div class="ml-2 d-inline">
                    <v-btn text small class="primary--text" v-if="!changeActivated" @click="activateChange">Promijeni kategorizaciju</v-btn>
                    <span v-else>
                        <v-btn text small class="primary--text" @click="changeCategories">Spremi promjene</v-btn>   
                        <v-btn text small class="red--text" @click="cancelChanges">Odustani</v-btn>   
                    </span>   
                </div>
            </v-col>
        </v-row>

        <!-- Kartice s kategorijama -->
        <v-row dense>
            <v-col cols="12" md="4">
                <v-card
                    color="#385F73"
                    dark
                    class="pa-2"
                >
                    <v-card-title class="text-h5">
                        1. kategorija
                    </v-card-title>

                    <v-card-subtitle>
                        do  <span v-if="!changeActivated">{{ categories.kategorija1_granica }}</span>
                        <v-text-field v-else v-model="categories.kategorija1_granica" class="editable-text"></v-text-field>
                        m<sup>3</sup>
                    </v-card-subtitle>

                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-chip color="primary"> 
                            <span v-if="!changeActivated">{{ categories.kategorija1_cijena }}</span>
                            <v-text-field v-else v-model="categories.kategorija1_cijena" class="editable-text"></v-text-field>
                            KM 
                        </v-chip>
                    </v-card-actions>
                </v-card>
            </v-col>
            <v-col cols="12" md="4">
                <v-card
                    color="#385F73"
                    dark
                    class="pa-2"
                >
                    <v-card-title class="text-h5">
                        2. kategorija
                    </v-card-title>

                    <v-card-subtitle>
                        od  <span v-if="!changeActivated">{{ categories.kategorija1_granica }}</span>
                        <v-text-field v-else v-model="categories.kategorija1_granica" class="editable-text"></v-text-field>
                        m<sup>3</sup>
                        do  <span v-if="!changeActivated">{{ categories.kategorija2_granica }}</span>
                        <v-text-field v-else v-model="categories.kategorija2_granica" class="editable-text"></v-text-field>
                        m<sup>3</sup>
                    </v-card-subtitle>

                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-chip color="primary"> 
                            <span v-if="!changeActivated">{{ categories.kategorija2_cijena }}</span>
                            <v-text-field v-else v-model="categories.kategorija2_cijena" class="editable-text"></v-text-field>
                            KM 
                        </v-chip>
                    </v-card-actions>
                </v-card>
            </v-col>
            <v-col cols="12" md="4">
                <v-card
                    color="#385F73"
                    dark
                    class="pa-2"
                >
                    <v-card-title class="text-h5">
                        3. kategorija
                    </v-card-title>

                    <v-card-subtitle>
                        preko  <span v-if="!changeActivated">{{ categories.kategorija2_granica }}</span>
                        <v-text-field v-else v-model="categories.kategorija2_granica" class="editable-text"></v-text-field>
                        m<sup>3</sup>
                    </v-card-subtitle>

                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-chip color="primary"> 
                            <span v-if="!changeActivated">{{ categories.kategorija3_cijena }}</span>
                            <v-text-field v-else v-model="categories.kategorija3_cijena" class="editable-text"></v-text-field>
                            KM 
                        </v-chip>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
        
        <v-row >
            <v-col>
                <p v-if="!changeActivated & !isLoading">Kategorizacija aktivna od {{ categories.date_created.replaceAll("-", ".") }}.</p>
                <p v-else class="accent--text">Unesite ograničenja i cijene za novu kategorizaciju.</p>
            </v-col>
        </v-row>
        
    </v-container>
</template>

<script>
import { mapGetters } from "vuex"

export default {
    name: "adminConsuptionCategories",
    data: () => ({
        //categories: { id:1,	date_created:"10.2.2022", kategorija1_cijena:"0,90", kategorija2_cijena:"1,20", kategorija3_cijena:"1,60", kategorija1_granica: "15", kategorija2_granica: "25"	},
        changeActivated: false
    }),
    mounted() {
        this.fetchCategories()
    },
    methods: {
        activateChange() {
            console.log("change activated")
            this.changeActivated = true
        },
        cancelChanges() {
            this.changeActivated = false
        },
        fetchCategories() {
          this.$store
              .dispatch('adminConsuptionCategories/fetchCategories', null, {root: true})
        },
        changeCategories() {
            this.$store
                .dispatch('adminConsuptionCategories/changeCategories', this.categories, { root: true })
                .catch( err => {
                    console.log(err)
                })
                this.changeActivated = false
        }
        
    },
    computed: {
        ...mapGetters('adminConsuptionCategories', ['isLoading', 'categories'])
   } 
}
</script>

<style>
.editable-text {
    display: inline-block !important;
    max-width: 65px !important;
} 
</style>