<template>
        <v-container blue lighten-5 fluid fill-height>
            <v-row align="center" class="">
                <v-col class="">
                    <v-img src="@/assets/img/logo.png" max-width="65px" class="mx-auto mb-6"></v-img>
                    <v-card class="mx-auto" max-width="600px" min-width="250px" flat>
                        <v-card-text class="py-10">
                            <h3 class="display-1 text-center">Novi račun</h3>
                            <p class="caption text-center py-2">Unesite potrebne podatke.</p>

                            <v-form ref="registerForm" lazy-validation v-model="valid"> 
                                <v-row>
                                    <!--Data -->
                                    <v-col cols="10" class="mx-auto">
                                        <v-text-field v-model="ime" :rules="[rules.required]" label="Ime" maxlength="20" required></v-text-field>
                                    </v-col>
                                    <v-col cols="10" class="mx-auto">
                                        <v-text-field v-model="prezime" :rules="[rules.required]" label="Prezime" maxlength="20" required></v-text-field>
                                    </v-col>
                                    <v-col cols="10" class="mx-auto">
                                        <v-text-field v-model="email" :rules="emailRules" label="E-mail" required></v-text-field>
                                    </v-col>
                                    <v-col cols="10" class="mb-2 mx-auto">
                                        <v-text-field v-model="password" :append-icon="showPassword?'mdi-eye':'mdi-eye-off'" :rules="[rules.required]" :type="showPassword ? 'text' : 'password'" name="input-10-1" label="Lozinka" counter @click:append="showPassword = !showPassword"></v-text-field>
                                    </v-col>
                                    <!--Register btn -->
                                    <v-col cols="10" class="mx-auto">
                                        <v-btn block class="primary" :disabled="!valid" @click="register">Izradi račun</v-btn>
                                    </v-col> 
                                </v-row>
                            </v-form>
                            

                        </v-card-text>

                        

                    </v-card>
                    <p class="text-center body-2 mt-7">Već imam račun. <router-link to="/prijava" class="rm-underline">Prijava</router-link> </p>
                </v-col>
            </v-row>
        </v-container>
</template>

<script>
export default {
    name: "Register",
    data: () => ({
        valid: false,
        ime: "",
        prezime: "",
        password: "",
        email: "",
        emailRules: [
        v => !!v || "Obavezno polje.",
        v => /.+@.+\..+/.test(v) || "Unesite ispravnu e-mail adresu."
        ],
        rules: {
        required: value => !!value || "Obavezno polje.",
        },
        showPassword: false
    }),
    methods: {
        // metoda za registraciju
        register() {
        if (this.$refs.registerForm.validate()) {
            const USER = {
                email: this.email,
                username: this.ime,
                userlastname: this.prezime,
                password: this.password,
            }
            console.log(USER)
            this.$store
                .dispatch('auth/register', USER, { root: true })
                .catch( err => {
                    console.log("Greska pri registraciji: " + err)
                })
            }
        },
    }
}
</script>

<style>
.rm-underline {
    text-decoration: none;
}
</style>