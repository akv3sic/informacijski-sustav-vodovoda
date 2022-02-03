<template>
    <div class="flex my-2">
        <v-card flat>
            <v-row>
                <v-col md="3" cols="12" sm="5">
                    <v-img :src=imgSrc height="200px"></v-img>
                </v-col>
                <v-col md="9" cols="12" sm="7">
                    <v-card-title> {{ title }} </v-card-title>
                    <v-card-text> {{ content }} </v-card-text>
                    <v-card-text class="grey--text">
                            Objavljeno: {{ published }}
                    </v-card-text>
                </v-col>
            </v-row>
        </v-card>
    </div>
</template>

<script>
export default {
    name: "HorizontalPost",
    props: {
        title: { type: String, required: true },
        published: { type: String, required: true },
        imgSrc: { type: String, required: true },
        content: { type: String, required: true },
    }
}
</script>