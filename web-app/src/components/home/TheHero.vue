<template>
    <section id="hero">
        <v-container>
            <v-row class="py-5" align="center">
                <v-col cols="12" md="6">
                    <h1 class="ml-4">Informacijski sustav vodovoda</h1>
                    <p class="ml-4">
                        <span class="light-blue--text text--darken-4">Fusce sed lacus pulvinar</span> urna molestie commodo vel eu leo.
                        Sed pellentesque elit ultricies massa vestibulum, elementum dignissim nulla tempor.
                        Donec enim enim, imperdiet a metus et, tristique ultrices mauris.</p>
                </v-col>
                <v-col cols="12" md="6">
                    <v-img 
                    src="@/assets/img/vodovod-brojilo.png"
                    max-height="400px"
                    contain
                    >
                    </v-img>
                </v-col>
            </v-row>
        </v-container>
    </section>
</template>

<script>
export default {
    name: "Hero"
}
</script>