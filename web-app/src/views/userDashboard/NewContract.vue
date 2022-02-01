<template>
    <v-container class="pa-2" :class="{ 'max-85 pa-16': $vuetify.breakpoint.mdAndUp }">
        <h2 class="mb-2">Zahtjev za novi priključak</h2>

        <v-row class="mb-5">
            <v-col>
                <span class="accent--text"> Lorem ipsum dolor sit amet consectetur, adipisicing elit. Suscipit excepturi dicta atque modi molestias adipisci. </span>
            </v-col>
        </v-row>

        <!-- forma -->
        <v-form ref="newContract" :class="{ 'newContractForm': $vuetify.breakpoint.mdAndUp }">
            <!-- ulica i kucni broj -->
            <v-row>
                <v-col cols="12" sm="8">
                    <v-text-field
                        v-model="contract.ulica"
                        label="Ulica"
                    >
                        <v-icon
                            slot="prepend"
                        >
                        mdi-road
                        </v-icon>
                    </v-text-field>
                </v-col>
                <v-col cols="12" sm="4">
                    <v-text-field
                        v-model="contract.kucniBroj"
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
                        label="Uplatnica"
                    ></v-file-input>
                </v-col>
            </v-row>
            <v-row>
                <v-col>
                    <v-file-input
                        show-size
                        accept="image/*,.pdf"
                        label="Katastarski plan"
                    ></v-file-input>
                </v-col>
            </v-row>
            <v-row>
                <v-col>
                    <v-file-input
                        show-size
                        accept="image/*,.pdf"
                        label="ZK izvadak"
                    ></v-file-input>
                </v-col>
            </v-row>
        </v-form>
        <!-- kraj forme -->


        <div class="actions py-7">
            <v-btn class="primary" @click="sendRequest">Pošalji zahtjev</v-btn>
        </div>
    </v-container>
</template>

<script>
export default {
    name: "NewContractRequest",
    data: () => ({
        contract: {
            ulica: "",
            kucniBroj: "",
        },
    }),
    methods: {
        sendRequest(){
            console.log(this.malfunctionReport)
        }
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