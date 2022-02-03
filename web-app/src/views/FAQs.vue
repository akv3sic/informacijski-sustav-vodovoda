<template>
    <div>
        <Header />
        <v-container :class="{'pa-16': $vuetify.breakpoint.lgAndUp}">
            <HeadingWithImage title="Često postavljana pitanja" height="33vh"/>
            <v-row>
                <!-- PITANJA I ODGOVORI -->
                <v-col cols="12" md="7" class="mt-8">
                      <v-expansion-panels class="pa-4">
                        <v-expansion-panel
                        v-for="(item,i) in 7"
                        :key="i"
                        class="my-2 py-2"
                        >
                        <v-expansion-panel-header>
                            Sed do eiusmod tempor ut labore?
                            <template v-slot:actions>
                                <v-icon color="primary">
                                $expand
                                </v-icon>
                            </template>
                        </v-expansion-panel-header>
                        <v-expansion-panel-content>
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                            <div class="d-flex justify-end mt-2">
                            <span class="text-caption mx-1">Korisno?</span>
                                <v-btn
                                    icon
                                    color="grey"
                                    x-small
                                    class="mx-1"
                                >
                                    <v-icon>mdi-thumb-up</v-icon>
                                </v-btn>
                                <v-btn
                                    icon
                                    color="grey"
                                    x-small
                                    class="mx-1"
                                >
                                    <v-icon>mdi-thumb-down</v-icon>
                                </v-btn>
                            </div>

                        </v-expansion-panel-content>
                        </v-expansion-panel>
                    </v-expansion-panels>
                </v-col>

                <!--  Forma za postavljanje novih pitanja -->
                <v-col cols="12" md="5" lg="4">
                    <v-card class="mx-auto new-question-form">
                        <v-card-text class="py-10">
                            <h3 class="display-1 text-center">Novo pitanje?</h3>
                            <p class="caption text-center py-2 accent--text">Ukoliko niste pronašli što vas zanima, slobodno nam se obratite.</p>

                            <v-form ref="loginForm" lazy-validation> 
                                <v-row>
                                    <!-- E-mail -->
                                    <v-col cols="10" class="mx-auto">
                                        <v-text-field v-model="question.email" :rules="emailRules" label="E-mail" required></v-text-field>
                                    </v-col>
                                    <!-- Ime -->
                                    <v-col cols="10" class="mb-2 mx-auto">
                                        <v-text-field v-model="question.name" label="Ime" counter></v-text-field>
                                    </v-col>
                                    <!-- Pitanje -->
                                    <v-col cols="10" class="mb-2 mx-auto">
                                            <v-textarea
                                            v-model="question.question"
                                            counter
                                            label="Pitanje"
                                        ></v-textarea>
                                    </v-col>
                                    <!-- Button -->
                                    <v-col cols="10" class="mx-auto">
                                        <v-btn block class="primary">Pošalji</v-btn>
                                    </v-col> 
                                </v-row>
                            </v-form>
                        </v-card-text>
                    </v-card>
                </v-col>

            </v-row>
        </v-container>
        
    </div>
</template>

<script>
import Header from "@/components/layout/TheHeader"
import HeadingWithImage from "@/components/layout/HeadingWithImage"

export default {
    name: "FAQs",
    components: { Header, HeadingWithImage },
    data: () => ({
        question: {
            email: "",
            name: "",
            question: ""
        },
        emailRules: [
            v => !!v || "Obavezno polje.",
            v => /.+@.+\..+/.test(v) || "Unesite ispravnu e-mail adresu."
        ],
        rules: {
            question: v => v.length <= 25 || 'Maksimalno 150 znakova'
        },
    })

}
</script>

<style scoped>
.new-question-form {
    transform: translate(0px, -40px);
}
</style>