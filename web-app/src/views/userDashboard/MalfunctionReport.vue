<template>
    <v-container>
        <h2 class="mb-2">Prijava kvara</h2>

        <v-row class="mb-5">
            <v-col>
                <span class="accent--text">Prijavite problem/kvar na vodovodnoj mreži ili u informacijskom sustavu.</span>
            </v-col>
            <!--
                <v-col>
                <v-btn class="primary" to="prijava-kvara/povijest-prijava">Povijest prijava</v-btn>
            </v-col>
            -->
        </v-row>

        <!-- forma -->
        <v-form ref="malfunctionReport">
            <v-row>
                <v-col>
                    <v-text-field
                        v-model="malfunctionReport.naslov"
                        label="Naslov"
                        :rules="[rules.required, rules.max50]"
                    ></v-text-field>
                </v-col>
            </v-row>
            <v-row>
                <v-col>
                    <v-textarea
                        v-model="malfunctionReport.opis_kvara"
                        label="Opis kvara"
                        counter
                        :rules="[rules.required, rules.max600]"
                    ></v-textarea>
                </v-col>
            </v-row>
            <div class="actions py-7">
                <v-btn class="primary" @click="sendReport">Pošalji prijavu</v-btn>
            </div>
        </v-form>
    </v-container>
</template>

<script>
export default {
    name: "MalfunctionReport",
    data: () => ({
        malfunctionReport: {
            naslov: "",
            opis_kvara: "",
        },
        // form rules
        rules: {
            required: value => !!value || "Obavezno polje.",
            max50: value => value.length < 50 || "Maksimalno 50 znakova.",
            max600: value => value.length < 600 || "Maksimalno 600 znakova.",
        },
    }),
    methods: {
        sendReport(){
            if(this.$refs.malfunctionReport.validate()) {
                this.$store.dispatch('userMalfunctionReport/postMalfunctionReport', this.malfunctionReport, { root: true })
                            .catch(err => { 
                                console.log(err)
                                reject(err)
                                })
            }
        }
    }    
}
</script>

<style>

</style>