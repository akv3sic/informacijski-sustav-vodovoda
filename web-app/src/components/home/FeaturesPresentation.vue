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

                        <v-card-subtitle>
                            {{ feature.description }}
                        </v-card-subtitle>
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
            { id: 1, name: "Feature Name", description: "Odio pellentesque diam volutpat commodo sed egestas. Turpis nunc eget lorem dolor sed.", icon: "mdi-domain" },
            { id: 2, name: "Feature Name", description: "Odio pellentesque diam volutpat commodo sed egestas. Turpis nunc eget lorem dolor sed.", icon: "mdi-domain" },
            { id: 3, name: "Feature Name", description: "Odio pellentesque diam volutpat commodo sed egestas. Turpis nunc eget lorem dolor sed.", icon: "mdi-domain" },
        ]
    })
}
</script>