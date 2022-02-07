<template>
    <v-container class="pa-16 max-85">
        <h2 class="mb-2">Moji podatci</h2>
        <v-row>
            <v-col>
                <v-text-field
                v-model="user.username"
                    label="Ime"
                ></v-text-field>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-text-field
                v-model="user.userlastname"
                    label="Prezime"
                ></v-text-field>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-text-field
                v-model="user.email"
                    disabled
                    label="E-mail adresa"
                ></v-text-field>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-text-field
                v-model="user.telefon"
                    label="Broj mobitela"
                ></v-text-field>
            </v-col>
        </v-row>
        <div class="actions py-7">
            <v-btn class="primary" @click="updateUserDetails">Spremi promjene</v-btn>
        </div>
    </v-container>
</template>

<script>
import { mapGetters } from "vuex"

export default {
    name: "AccountDetails",
    data: () => ({

    }),
    created() {
        this.fetchUserDetails();
    },
    methods: {
        fetchUserDetails() {
            this.$store
                .dispatch('userAccountDetails/fetchUserDetails', null, {root: true})
        },
        updateUserDetails() {
            this.$store
                .dispatch('userAccountDetails/updateUserDetails', this.user, { root: true })
                .catch( err => {
                    console.log(err)
                })
        }
    },
    computed: {
        ...mapGetters('userAccountDetails', ['isLoading', 'user'])
   } 
}
</script>

<style>
.max-85 {
    max-width: 85vw;
}
</style>