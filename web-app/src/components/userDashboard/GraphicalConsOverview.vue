<template>
<v-card
    class="mt-4"
    max-width="50vw"
  >
    <v-sheet
      class="v-sheet--offset mx-auto"
      color="cyan"
      elevation="12"
      max-width="calc(100% - 32px)"
    >
      <v-sparkline
        :labels="labels"
        :value="values"
        color="white"
        line-width="2"
        padding="16"
      ></v-sparkline>
    </v-sheet>

    <v-card-text class="pt-0">
      <div class="text-h6 font-weight-light my-2">
        Potrošnja (m<sup>3</sup>)
      </div>
      <div class="subheading font-weight-light grey--text">
        Zadnjih 12 mjeseci
      </div>
    </v-card-text>
</v-card>
</template>

<script>
export default {
    name: "GraphicalConsuptionOverview",
    props: {
      labels: { type: Array, required: true },
      values: { type: Array, required: true },
    }
}
</script>