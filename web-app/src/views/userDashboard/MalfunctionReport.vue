<template>
    <v-container class="pa-16 max-85">
        <h2 class="mb-2">Prijava kvara</h2>

        <v-row class="mb-5">
            <v-col>
                <span class="accent--text">Prijavite problem/kvar na vodovodnoj mreži ili u informacijskom sustavu.</span>
            </v-col>
            <v-col>
                <v-btn class="primary" to="prijava-kvara/povijest-prijava">Povijest prijava</v-btn>
            </v-col>
        </v-row>

        <!-- forma -->
        <v-row>
            <v-col>
                <v-radio-group v-model="malfunctionReport.type">
                    <v-radio
                        v-for="type in reportTypes"
                        :key="type.id"
                        :label="type.text"
                        :value="type.id"
                    ></v-radio>
                </v-radio-group>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-text-field
                    v-model="malfunctionReport.heading"
                    label="Naslov"
                ></v-text-field>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-textarea
                    v-model="malfunctionReport.description"
                    label="Opis kvara"
                    counter
                ></v-textarea>
            </v-col>
        </v-row>


        <div class="actions py-7">
            <v-btn class="primary" @click="sendReport">Pošalji prijavu</v-btn>
        </div>
    </v-container>
</template>

<script>
export default {
    name: "MalfunctionReport",
    data: () => ({
        malfunctionReport: {
            heading: "",
            description: "",
            type: 1
        },
        reportTypes: [
            { id: 1, text: "Kvar na vodovodnoj mreži" },
            { id: 2, text: "Kvar u informacijskom sustavu" }
        ]
    }),
    methods: {
        sendReport(){
            console.log(this.malfunctionReport)
        }
    }    
}
</script>

<style>
.max-85 {
    max-width: 85vw;
}
</style>