<template>
    <v-container>
        <v-row>
            <v-col>
                <span class="text-h5">Kategorije potrošnje</span>
                <div class="ml-2 d-inline">
                    <v-btn text small class="primary--text" to="proizvodi-dodaj-novi">Promijeni kategorizaciju</v-btn>   
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

                    <v-card-subtitle>do {{ kategorizacija.kategorija1_granica }} m<sup>3</sup> </v-card-subtitle>

                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-chip color="primary"> {{ kategorizacija.kategorija1_cijena }} KM </v-chip>
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
                        od {{ kategorizacija.kategorija1_granica }} m<sup>3</sup> 
                        do {{ kategorizacija.kategorija2_granica }} m<sup>3</sup> 
                    </v-card-subtitle>

                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-chip color="primary"> {{ kategorizacija.kategorija2_cijena }} KM </v-chip>
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

                    <v-card-subtitle>preko {{ kategorizacija.kategorija2_granica }} m<sup>3</sup> </v-card-subtitle>

                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-chip color="primary"> {{ kategorizacija.kategorija3_cijena }} KM </v-chip>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
        
        <v-row>
            <v-col>
                <p>Kategorizacija aktivna od {{ kategorizacija.date_created }}</p>
            </v-col>
        </v-row>
        
    </v-container>
</template>

<script>
export default {
    name: "adminConsuptionCategories",
    data: () => ({
        kategorizacija: { id:1,	date_created:"10.2.2022", kategorija1_cijena:"0,90", kategorija2_cijena:"1,20", kategorija3_cijena:"1,60", kategorija1_granica: "15", kategorija2_granica: "25"	}
    })
}
</script>