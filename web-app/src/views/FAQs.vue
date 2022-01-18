<template>
    <div>
        <Header />
        <v-container class="pa-16">
            <HeadingWithImage />
            <v-row>
                <!-- PITANJA I ODGOVORI -->
                <v-col cols="7" class="mt-8">
                      <v-expansion-panels class="pa-4">
                        <v-expansion-panel
                        v-for="(item,i) in 7"
                        :key="i"
                        class="my-2 py-2"
                        >
                        <v-expansion-panel-header>
                            Pitanje se nalazi ovdje?
                            <template v-slot:actions>
                                <v-icon color="primary">
                                $expand
                                </v-icon>
                            </template>
                        </v-expansion-panel-header>
                        <v-expansion-panel-content>
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                            <div class="d-flex justify-end mt-2">
                            <span class="text-caption mx-1">Korisno?</span>
                                <v-btn
                                    icon
                                    color="grey"
                                    x-small
                                    class="mx-1"
                                >
                                    <v-icon>mdi-thumb-up</v-icon>
                                </v-btn>
                                <v-btn
                                    icon
                                    color="grey"
                                    x-small
                                    class="mx-1"
                                >
                                    <v-icon>mdi-thumb-down</v-icon>
                                </v-btn>
                            </div>

                        </v-expansion-panel-content>
                        </v-expansion-panel>
                    </v-expansion-panels>
                </v-col>
                <v-col cols="3">sa strane pitanje mi novo postavi</v-col>
            </v-row>
        </v-container>
        
    </div>
</template>

<script>
import Header from "@/components/layout/TheHeader"
import HeadingWithImage from "@/components/layout/HeadingWithImage"

export default {
    name: "FAQs",
    components: { Header, HeadingWithImage }
}
</script>