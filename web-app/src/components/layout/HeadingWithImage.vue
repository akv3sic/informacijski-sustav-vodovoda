<template>
    <v-card rounded="lg">
        <v-img
        src="@/assets/img/faq-banner.png"
        class="white--text align-end"
        gradient="to left bottom, rgba(0,0,0,.3), rgba(0,0,0,.8)"
        :height="height"
        >
        <v-card-title v-text="title" class="display-1"></v-card-title>
        <v-card-actions>
        <v-spacer></v-spacer>
        <!-- 
            Prostor za akcije ovdje
        -->
        </v-card-actions>
        </v-img>
    </v-card>
</template>

<script>
export default {
    name: "HeadingWithImage",
    data: () => ({
        imgSrc: "",
        title: "Često postavljana pitanja",
        height: "33vh"
    })
}
</script>