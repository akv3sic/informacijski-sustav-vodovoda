<template>
<v-card
    class="mt-4"
>

      <v-sparkline
        :labels="labels"
        :value="values"
        color="indigo darken-2"
        line-width="2"
        padding="16"
      ></v-sparkline>

    <v-card-text class="pt-0">
      <div class="text-h6 font-weight-light my-2 accent--text">
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