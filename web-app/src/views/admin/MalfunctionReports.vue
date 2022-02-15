<template>
    <v-container>
        <v-row>
            <v-col>
                <span class="text-h5">Pregled kvarova</span>
            </v-col>
        </v-row>

        <v-row>
            <v-col>
                <v-sheet elevation="6">
                    <v-tabs
                    background-color="primary"
                    dark
                    v-model="activeTab"
                    >
                    <v-tabs-slider color="white"></v-tabs-slider>
                    <v-tab
                        v-for="(tab, index) in tabs"
                        :key="index"
                    >
                        {{ tab }}  
                    </v-tab>
                    </v-tabs>
                </v-sheet>

                <MalfunctionReportCard
                    v-for="report in malfunctionReports"
                    :key="report.id"
                    :report="report"
                > 
                </MalfunctionReportCard>

            </v-col>
        </v-row>
        
    </v-container>
</template>

<script>
import { mapGetters } from "vuex"
import MalfunctionReportCard from "@/components/admin/MalfunctionReportCard"

export default {
    name: "adminMalfunctionReports",
    components: { MalfunctionReportCard },
    data () {
      return {
        //activeTab: null,
        tabs: [
          'Svi','Aktivni', 'Završeni'
        ],
        /*malfunctionReports: [
            { id: 1, naslov: "lorem ipsum", opis_kvara: "opis kvara lorem ipsum sit dolor amen", korisnik: "Jure Jurić", status: "Aktivan" },
            { id: 2, naslov: "lorem ipsum", opis_kvara: "opis kvara lorem ipsum sit dolor amen", korisnik: "Jure Jurić", status: "Završen" },
            { id: 3, naslov: "lorem ipsum", opis_kvara: "opis kvara lorem ipsum sit dolor amen", korisnik: "Jure Jurić", status: "Aktivan" }
        ]*/
      }
    },
    mounted() {
        this.fetchReports()
    },
    methods: {
        fetchReports(id) {
            this.$store
                .dispatch('adminMalfunctionReports/fetchMalfunctionReports', id, {root: true})
        },
        
    },
    watch: {
        activeTab(newTab) {
            console.log("odabrani tab promijenjen na " + newTab)
            this.fetchReports(newTab)
        }
    },
    computed: {
        ...mapGetters('adminMalfunctionReports', ['isLoading', 'malfunctionReports']),

        activeTab: {
            get () {
            return this.$store.getters['adminMalfunctionReports/activeTab']
            },
            set (val) {
            this.$store.dispatch('adminMalfunctionReports/setActiveTab', val)
            },
        },
    }
}
</script>

<style>
.report-card {
    border-left: 7px solid green !important;
}  
</style>