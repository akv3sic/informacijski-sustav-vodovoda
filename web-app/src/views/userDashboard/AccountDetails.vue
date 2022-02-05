<template>
    <v-container class="pa-16 max-85">
        <h2 class="mb-2">Moji podatci</h2>
        <v-row>
            <v-col>
                <v-text-field
                v-model="user.ime"
                    label="Ime"
                ></v-text-field>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-text-field
                v-model="user.prezime"
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
                v-model="user.mobitel"
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
export default {
    name: "AccountDetails",
    data: () => ({
        user: {
            ime: "Ivo",
            prezime: "Ivić",
            email: "ivo@lorem.ipsum",
            mobitel: "+387 77 123 456",
        }
    }),
    created() {
        this.fetchUserDetails();
    },
    methods: {
        fetchUserDetails() {
            this.$store
                .dispatch('userAccountDetails/fetchUserDetails', null, {root: true})
        },
        updateUserDetails(){
            console.log(this.user)
        }
    }    
}
</script>

<style>
.max-85 {
    max-width: 85vw;
}
</style>