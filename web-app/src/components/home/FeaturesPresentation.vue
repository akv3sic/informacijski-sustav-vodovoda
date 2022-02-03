<template>
    <section id="features">
        <v-container>
            <v-row class="py-5" align="center">
                <v-col cols="12" md="6" v-for="feature in features" :key="feature.id"  class="d-flex justify-center align-center">
                    <v-card
                        :class="{'mx-auto': $vuetify.breakpoint.smAndDown}"
                        max-width="344"
                        flat
                        class="bounce"
                    >
                        <v-card-text>
                            <v-icon
                                color="accent"
                                large
                            >
                                {{ feature.icon }}
                            </v-icon>
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
            { id: 1, name: "Pregled potrošnje", description: "Odio pellentesque diam volutpat commodo sed egestas. Turpis nunc eget lorem dolor sed.", icon: "mdi-chart-waterfall" },
            { id: 2, name: "Nadzor gubitaka", description: "Odio pellentesque diam volutpat commodo sed egestas. Turpis nunc eget lorem dolor sed.", icon: "mdi-water-alert" },
            { id: 3, name: "Plaćanje računa", description: "Odio pellentesque diam volutpat commodo sed egestas. Turpis nunc eget lorem dolor sed.", icon: "mdi-cash" },
            { id: 4, name: "Korisnička podrška", description: "Odio pellentesque diam volutpat commodo sed egestas. Turpis nunc eget lorem dolor sed.", icon: "mdi-offer" },
        ]
    })
}
</script>

<style>
.bounce:hover,
.bounce:hover:active {
  animation: bounce 0.6s ease;
  -webkit-animation: bounce 0.6s ease;
}

@keyframes bounce {
  0% {
    top: 0px;
  }
  25% {
    top: -10px;
  }
  50% {
    top: 5px;
  }
  75% {
    top: -5px;
  }
  100% {
    top: 0px;
  }
}

@-webkit-keyframes bounce {
  0% {
    top: 0px;
  }
  25% {
    top: -10px;
  }
  50% {
    top: 5px;
  }
  75% {
    top: -5px;
  }
  100% {
    top: 0px;
  }
}

</style>