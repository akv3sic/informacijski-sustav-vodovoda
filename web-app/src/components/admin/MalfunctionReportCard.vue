<template>
    <div>
        <v-card
            class="pa-1 my-2"
            :class="{'report-card-active': report.status.status == 'Aktivan', 'report-card-finished': report.status.status != 'Aktivan'}"
            outlined
            min-height="100px"
        >
            <v-row>
            <v-col cols="4" class="">
                <v-card-title> {{ report.naslov }} </v-card-title>
                <v-card-subtitle> 
                    <v-icon class="xs" small>mdi-account</v-icon>
                    {{ report.korisnik.username }} {{ report.korisnik.userlastname }} 
                </v-card-subtitle>
            </v-col>
            <v-col cols="4">
                <v-card-text>
                    <h5>Opis kvara:</h5>
                    {{ report.opis_kvara }}
                </v-card-text>
            </v-col>
            <v-col cols="4">
                <v-card-text>
                    <h5>Status:</h5>
                    <v-chip :class="{'orange': report.status.status == 'Aktivan'}" class="green" dark>
                        {{ report.status.status }}  
                    </v-chip>
                </v-card-text>
                <v-card-actions>
                    <v-btn 
                    text 
                    small 
                    class="primary--text"
                    v-if="report.status.status == 'Aktivan'"
                    @click="changeStatusToFinished(report.id)"
                    >
                    Označi kao završeno
                    </v-btn>   
                </v-card-actions>
            </v-col>
            </v-row>
        </v-card>
    </div>
</template>

<script>
import { mapGetters } from "vuex"

export default {
    name: "malfunctionReportCard",
    props: {
        report: { type: Object, required: true }
    },
    methods: {
        changeStatusToFinished(id) {
            console.log(id)
            this.$store
                .dispatch('adminMalfunctionReports/changeReportStatus', id, {root: true})
                .then(
                    this.$store
                        .dispatch('adminMalfunctionReports/fetchMalfunctionReports', this.activeTab, {root: true})
                )
        }
    },
    computed: {
        ...mapGetters('adminMalfunctionReports', ['isLoading', 'activeTab']),
    }
}
</script>

<style>
.report-card-active {
    border-left: 7px solid orange !important;
}
.report-card-finished {
    border-left: 7px solid green !important;
}  
</style>