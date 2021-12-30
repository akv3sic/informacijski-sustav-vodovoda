<template>
    <section id="features">
        <v-container class="">
            <v-row class="py-5" align="center">
                <v-col cols="12" md="4" v-for="feature in features" :key="feature.id">
                    <v-card
                        :class="{'mx-auto': $vuetify.breakpoint.smAndDown}"
                        max-width="344"
                        flat
                    >
                        <v-card-text>
                            <v-icon>{{ feature.icon }}</v-icon>
                        </v-card-text>
                    

                        <v-card-title>
                            {{ feature.name }}
                        </v-card-title>

                        <v-card-text>
                            {{ feature.description }}
                        </v-card-text>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </section>
</template>

<script>
export default {
    name: "FeaturesPresentation",
    data: () => ({
        features: [
            { id: 1, name: "Popisivanje potrošnje", description: "Odio pellentesque diam volutpat commodo sed egestas. Turpis nunc eget lorem dolor sed.", icon: "mdi-gauge" },
            { id: 2, name: "Evidencija gubitaka", description: "Odio pellentesque diam volutpat commodo sed egestas. Turpis nunc eget lorem dolor sed.", icon: "mdi-water-alert" },
            { id: 3, name: "Plaćanje računa", description: "Odio pellentesque diam volutpat commodo sed egestas. Turpis nunc eget lorem dolor sed.", icon: "mdi-ticket-outline" },
        ]
    })
}
</script>