<template>
        <v-container blue lighten-5 fluid fill-height>
            <v-row align="center" class="">
                <v-col class="">
                    <v-img src="@/assets/img/logo.png" max-width="65px" class="mx-auto mb-6"></v-img>
                    <v-card class="mx-auto" max-width="600px" min-width="250px" flat>
                        <v-card-text class="py-10">
                            <h3 class="display-1 text-center">Prijava u sustav</h3>
                            <p class="caption text-center py-2">Unesite podatke kako bi pristupili vašem računu.</p>

                            <v-form ref="loginForm" lazy-validation v-model="valid"> 
                                <v-row>
                                    <!--Login credentials -->
                                    <v-col cols="10" class="mx-auto">
                                        <v-text-field v-model="email" :rules="emailRules" label="E-mail" required></v-text-field>
                                    </v-col>
                                    <v-col cols="10" class="mb-2 mx-auto">
                                        <v-text-field v-model="password" :append-icon="showPassword?'mdi-eye':'mdi-eye-off'" :rules="[rules.required]" :type="showPassword ? 'text' : 'password'" name="input-10-1" label="Lozinka" counter @click:append="showPassword = !showPassword"></v-text-field>
                                    </v-col>
                                    <!--Login btn -->
                                    <v-col cols="10" class="mx-auto">
                                        <v-btn block class="primary" :disabled="!valid">Prijava</v-btn>
                                    </v-col> 
                                </v-row>
                            </v-form>
                            

                        </v-card-text>

                        

                    </v-card>
                    <p class="text-center body-2 mt-7">Nemam račun. <router-link to="/registracija" class="rm-underline">Napravi račun</router-link> </p>
                    <p class="text-center body-2">Zaboravili ste lozinku? <router-link to="/resetiranje-lozinke" class="rm-underline">Resetiranje lozinke</router-link> </p>
                </v-col>
            </v-row>
        </v-container>
</template>

<script>
export default {
    name: "Login",
    data: () => ({
        valid: false,
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
    })
}
</script>

<style>
.rm-underline {
    text-decoration: none;
}
</style>