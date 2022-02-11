<template>
    <v-container>
        <v-row>
            <v-col>
                <span class="text-h5">Osoblje</span>
                <span class="text-h5 grey--text"> ({{ users.length }})</span>
                <div class="ml-2 d-inline">
                    <v-btn text small class="primary--text" to="proizvodi-dodaj-novi">Dodaj novog</v-btn>   
                </div>
            </v-col>
        </v-row>

        <!-- **** ZAGLAVLJE liste **** -->
        <v-row class="hidden-sm-and-down mt-1">
            <v-col class="text-left" cols="1">
                <v-icon class="mb-1">mdi-identifier</v-icon>
            </v-col>
            <v-col class="text-left" cols="2">
                Ime i prezime
            </v-col>
            <v-col class="text-left" cols="2">
                E-mail
            </v-col>
            <v-col class="text-left" cols="2">
                Telefon
            </v-col>
            <v-col class="text-left" cols="2">
                Adresa
            </v-col>
            <v-col class="text-left" cols="3">
                Uloga
            </v-col>
        </v-row>
        <!-- ************************** -->

        <!-- AKO se proizvodi učitavaju 
        <v-skeleton-loader v-if="isLoading" type="table-tbody@3" width="100%"></v-skeleton-loader>
         ************************** -->
        
        <!-- **** STAVKE liste **** -->
        <v-card
            v-for="user in users"
            :key="user.id"
            class="pa-1 my-2"
            outlined
        >
            <v-row>
            <v-col cols="6" md="1" sm="6" class="">
                <span class="text--caption hidden-md-and-up">ID:</span>
                {{ user.id }}
            </v-col>
            <v-col cols="6" md="2" sm="6">
                {{ user.username}} {{ user.userlastname}}
            </v-col>
            <v-col cols="6" md="2" sm="6">
                <v-row class="hidden-md-and-up"> 
                    <v-col class="text-caption">E-mail: </v-col>
                </v-row>
                {{ user.email}}
            </v-col><v-col cols="6" md="2" sm="6">
                <v-row class="hidden-md-and-up"> 
                    <v-col class="text-caption">Telefon</v-col>
                </v-row>
                {{ user.telefon }}
            </v-col><v-col cols="6" md="2" sm="6">
                <v-row class="hidden-md-and-up"> 
                    <v-col class="text-caption">Adresa</v-col>
                </v-row>
                {{ user.adresa }}
            </v-col>
            <v-col cols="6" md="2" sm="6">
                <v-row class="hidden-md-and-up"> 
                    <v-col class="text-caption">Uloga: </v-col>
                </v-row>
                {{ user.role }}
            </v-col>
            <v-col md="1">
                <v-icon @click="deleteuser(user.id, user.ime, user.url_slike)" class="ml-1">mdi-delete</v-icon>
                <router-link class="rm-underline" :to="'/admin/uredi-proizvod/' + user.id + '/' + user.slug">
                    <v-icon class="ml-1">mdi-pencil</v-icon>
                </router-link>
                <v-icon class="ml-1">mdi-card-account-details</v-icon>
            </v-col>
            </v-row>
        </v-card>
        <!-- ************************** -->
    </v-container>
</template>

<script>
import { mapGetters } from "vuex"
import Swal from 'sweetalert2'

export default {
    name: 'adminCustomers',
    data: () => ({
       users: [
           { id: 1, username: "John", userlastname: "Doe", email: "test@johndoe.test", telefon: "+387 63 611 611", adresa: "Street 22", dateJoined: "10.2.2022.", role: "Administrator"},
           { id: 2, username: "John", userlastname: "Doe", email: "test@johndoe.test", telefon: "+387 63 611 611", adresa: "Street 22", dateJoined: "10.2.2022.", role: "Popisivač"},
           { id: 5, username: "John", userlastname: "Doe", email: "test@johndoe.test", telefon: "+387 63 611 611", adresa: "Street 22", dateJoined: "10.2.2022.", role: "Popisivač"},
           { id: 8, username: "John", userlastname: "Doe", email: "test@johndoe.test", telefon: "+387 63 611 611", adresa: "Street 22", dateJoined: "10.2.2022.", role: "Administrator"},
       ]
    }),
    mounted() {
        //this.fetchusers();
    },
    methods: {
        fetchusers() {
            this.$store
                .dispatch('users/fetchusers', {categoryId: null}, {root: true})
        },
        deleteuser(userId, userName, userImageUrl) {
            /* confirmation dialog */
            Swal.fire({
                title: 'Sigurno želite izbrisati ovaj proizvod?',
                text: userName,
                imageUrl: userImageUrl,
                imageHeight: 135,
                showDenyButton: true,
                confirmButtonText: `Da, izbriši`,
                confirmButtonColor: '#052949',
                denyButtonText: 'Ne',
                denyButtonColor: '#c52033',
                customClass: {
                confirmButton: 'order-2',
                denyButton: 'order-3',
                }
            }).then((result) => {
                if (result.isConfirmed) {
                this.$store
                .dispatch('user/deleteuser', userId, {root: true})
                this.fetchusers()
                }
            })
        /*********************************/
        }
    },
    computed: {
        //...mapGetters('users', ['users', 'isLoading'])
    },
}
</script>

<style scoped>
.rm-underline{
    text-decoration: none;
}
</style>