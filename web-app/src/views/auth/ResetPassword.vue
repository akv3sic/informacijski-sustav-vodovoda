<template>
        <v-container blue lighten-5 fluid fill-height>
            <v-row align="center" class="">
                <v-col class="">
                    <v-img src="@/assets/img/logo.png" max-width="65px" class="mx-auto mb-6"></v-img>
                    <v-card class="mx-auto" max-width="600px" min-width="250px" flat>
                        <v-card-text class="py-10">
                            <h3 class="display-1 text-center">Zaboravili ste lozinku?</h3>
                            <p class="caption text-center py-2">Bez brige, poslat ćemo vam upute za oporavak računa na e-mail.</p>

                            <v-form ref="resetPasswordForm" lazy-validation v-model="valid"> 
                                <v-row>
                                    <!--Used mail -->
                                    <v-col cols="10" class="mx-auto">
                                        <v-text-field v-model="email" :rules="emailRules" label="E-mail" required></v-text-field>
                                    </v-col>
                                    <!-- Reset btn -->
                                    <v-col cols="10" class="mx-auto">
                                        <v-btn block class="primary" :disabled="!valid">Pošalji</v-btn>
                                    </v-col> 
                                </v-row>
                            </v-form>
                            

                        </v-card-text>

                    </v-card>
                    <p class="text-center body-2 mt-7">
                        <v-icon class="mx-1">mdi-arrow-left</v-icon>
                        <router-link to="/prijava" class="rm-underline">Natrag na prijavu</router-link>
                    </p>
                </v-col>
            </v-row>
        </v-container>
</template>

<script>
export default {
    name: "ResetPassword",
    data: () => ({
        valid: false,

        email: "",
        emailRules: [
        v => !!v || "Obavezno polje.",
        v => /.+@.+\..+/.test(v) || "Unesite ispravnu e-mail adresu."
        ],
        rules: {
        required: value => !!value || "Obavezno polje.",
        },
        showPassword: false
    })
}
</script>

<style>
.rm-underline {
    text-decoration: none;
}
</style>