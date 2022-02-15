<template>
    <v-container class="pa-2" :class="{ 'max-85 pa-16': $vuetify.breakpoint.mdAndUp }">
        <h2 class="mb-2">Zahtjev za novi priključak</h2>

        <v-row class="mb-5">
            <v-col>
                <span class="accent--text"> Lorem ipsum dolor sit amet consectetur, adipisicing elit. Suscipit excepturi dicta atque modi molestias adipisci. </span>
            </v-col>
        </v-row>

        <!-- SUCCESS ALERT -->
        <v-alert v-if="successAlert" type="success">Vaš zahtjev je uspješno poslan.</v-alert>

        <!-- forma -->
        <v-form ref="newContract" :class="{ 'newContractForm': $vuetify.breakpoint.mdAndUp }">
            <!-- ulica i kucni broj -->
            <v-row>
                <v-col cols="12" sm="4">
                    <v-select
                    v-model="selectedPlace"
                    :items="places"
                    item-text="mjesto"
                    label="Mjesto"
                    prepend-icon="mdi-city"
                    ></v-select>
                </v-col>
                <v-col cols="12" sm="4">
                    <v-select
                    v-model="selectedStreet"
                    :items="streets"
                    item-text="ulica"
                    label="Ulica"
                    prepend-icon="mdi-road"
                    no-data-text="Izaberite mjesto"
                    ></v-select>
                </v-col>
                <v-col cols="12" sm="4">
                    <v-text-field
                        v-model="contract.kucni_broj"
                        label="Kućni broj"
                    >
                        <v-icon
                            slot="prepend"
                        >
                        mdi-numeric-2-box-outline
                        </v-icon>
                    </v-text-field>
                </v-col>
            </v-row>

            <!-- učitavanje dokumenata -->
            <v-row>
                <v-col>
                    <v-file-input
                        show-size
                        accept="image/*,.pdf"
                        label="Zahtjev i dokaz o uplati"
                        v-model="contract.zahtjev"
                    ></v-file-input>
                </v-col>
            </v-row>
            <v-row>
                <v-col>
                    <v-file-input
                        show-size
                        accept="image/*,.pdf"
                        label="Katastarski plan"
                        v-model="contract.katastarski_plan"
                    ></v-file-input>
                </v-col>
            </v-row>
            <v-row>
                <v-col>
                    <v-file-input
                        show-size
                        accept="image/*,.pdf"
                        label="ZK izvadak"
                        v-model="contract.zk_izvadak"
                    ></v-file-input>
                </v-col>
            </v-row>

            <!--  PROGRESS -->
            <v-progress-linear
            :value="uploadProgress"
            v-if="uploadProgress"
            height="20"
            >
                <span class="subtitle-2"> {{ uploadProgress }}% </span>
            </v-progress-linear>


        </v-form>
        <!-- kraj forme -->
        

        <div class="actions py-7">
            <v-btn class="primary" @click="sendRequest">Pošalji zahtjev</v-btn>
        </div>
    </v-container>
</template>

<script>
import { mapGetters } from "vuex"

export default {
    name: "NewContractRequest",
    data: () => ({
        contract: {
            kucni_broj: "",
            zahtjev: null,
            zk_izvadak: null,
            katastarski_plan: null
        },
        selectedPlace: null,
        selectedStreet: null
    }),
    mounted() {
        this.fetchPlaces()
    },
    methods: {
        sendRequest(){
            this.contract['ulica'] = this.selectedStreet
            let formData = new FormData()
            formData.append('zahtjev', this.contract.zahtjev)
            formData.append('zk_izvadak', this.contract.zk_izvadak)
            formData.append('katastarski_plan', this.contract.katastarski_plan)
            formData.append('ulica', this.contract.ulica)
            formData.append('kucni_broj', this.contract.kucni_broj)

            // console.log(this.contract)
            this.$store
                .dispatch('userNewContractRequest/sendRequest', formData, {root: true})
        },
        fetchPlaces() {
            this.$store
                .dispatch('placesAndStreets/fetchPlaces', null, {root: true})
        },
        fetchStreets(place) {
            this.$store
                .dispatch('placesAndStreets/fetchStreets', place, {root: true})
        },
    },
    computed: {
        ...mapGetters('placesAndStreets', ['places', 'streets']),
        ...mapGetters('userNewContractRequest', ['isLoading', 'uploadProgress', 'successAlert']),
    },
    watch: {
        selectedPlace(newValue) {
            console.log("mjesto promijenjeno: " + newValue)
            this.fetchStreets(newValue)
        },
    }   
}
</script>

<style>
.max-85 {
    max-width: 85vw;
}
.newContractForm {
    max-width: 50vw;
}
</style>