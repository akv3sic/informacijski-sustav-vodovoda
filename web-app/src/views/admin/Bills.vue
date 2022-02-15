<template>
    <v-container class="">
        <h2 class="mb-2">Računi</h2>
        <v-row class="mb-1">
            <v-col>
                <span class="accent--text"> Lorem, ipsum dolor sit amet consectetur adipisicing.. </span>
            </v-col>
        </v-row>

        <v-row class="mb-1">
            <v-col>
                <span class=""> Broj računa za aktivaciju: {{ noOfBillsToBeActivated }}</span>

                <v-tooltip bottom>
                    <template v-slot:activator="{ on, attrs }">
                        <v-btn
                        color="primary"
                        v-bind="attrs"
                        v-on="on"
                        class="ml-5"
                        :disabled="noOfBillsToBeActivated == 0"
                        @click="activateBills"
                        >
                        Aktiviraj sve
                        </v-btn>
                    </template>
                    <span>Računi će se prikazati korisnicima s današnjim datumom dospijeća.</span>
                </v-tooltip>
            </v-col>
        </v-row>

        
    </v-container>
</template>

<script>
import { mapGetters } from "vuex"

export default {
    name: "AdminBills",
    data: () => ({

    }),
    mounted() {
        this.fetchNoOfBillsToActivate()
    },
    methods: {
        fetchNoOfBillsToActivate() {
            this.$store
                .dispatch('adminBills/fetchNoOfBillsToBeActivated', null, {root: true})
        },
        activateBills() {
            this.$store
                .dispatch('adminBills/activateAllBills', null, {root: true})
            this.fetchNoOfBillsToActivate()
        },
        
    },
    computed: {
        ...mapGetters('adminBills', ['isLoading', 'noOfBillsToBeActivated'])
    },
    watch: {
    }
}
</script>

<style>
.filter-item {
    max-width: 240px;
    margin: 0px 12px;
}   
</style>