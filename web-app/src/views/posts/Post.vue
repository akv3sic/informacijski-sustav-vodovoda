<template>
    <div>
        <Header />
        <v-container>
            <v-breadcrumbs :items="breadcrumbsItems"></v-breadcrumbs>
            <h2 class="display-1 pl-5 pb-2">Naslov članka</h2>
            <v-row class="pl-5">
                <v-col cols="4">
                    <v-icon class="mx-1" color="primary">mdi-account-outline</v-icon>
                    <p class="body-2 d-inline grey--text">Ante Kvesić</p>
                </v-col>
                <v-col cols="4">
                    <v-icon class="mx-1" color="primary">mdi-calendar</v-icon>
                    <p class="body-2 d-inline grey--text">3.1.2022.</p>
                </v-col>
            </v-row>
            <v-row class="px-8">
                <v-col>
                    <v-img 
                        src="https://www.blogtyrant.com/wp-content/uploads/2017/02/how-to-write-a-good-blog-post.png"
                        contain
                        max-width="1200px"
                        min-width="90px"
                    >
                    </v-img>  
                </v-col>

            </v-row>
            <v-row class="pl-5">
                <v-col xl="8">
                    <div class="mb-3">
                        <v-icon class="mx-1 facebook">mdi-facebook</v-icon>
                        <v-icon class="mx-1 whatsapp">mdi-whatsapp</v-icon>
                        <v-icon class="mx-1 print">mdi-printer</v-icon>
                        <v-icon class="mx-1 email">mdi-email</v-icon>
                    </div>

                    Adipiscing elit duis tristique sollicitudin nibh. Sed faucibus turpis in eu mi bibendum. Viverra orci sagittis eu volutpat odio facilisis mauris sit amet. Eu non diam phasellus vestibulum lorem sed. Maecenas volutpat blandit aliquam etiam erat velit.
                    Adipiscing elit duis tristique sollicitudin nibh. Sed faucibus turpis in eu mi bibendum. Viverra orci sagittis eu volutpat odio facilisis mauris sit amet. Eu non diam phasellus vestibulum lorem sed. Maecenas volutpat blandit aliquam etiam erat velit.
                    Adipiscing elit duis tristique sollicitudin nibh. Sed faucibus turpis in eu mi bibendum. Viverra orci sagittis eu volutpat odio facilisis mauris sit amet. Eu non diam phasellus vestibulum lorem sed. Maecenas volutpat blandit aliquam etiam erat velit.
                </v-col>
            </v-row>

        </v-container>
    </div>
</template>

<script>
import Header from '../../components/layout/TheHeader.vue'
export default {
    name: "Post",
    components: { Header },
    data: () => ({
      breadcrumbsItems: [
        {
          text: 'Naslovna',
          disabled: false,
          href: '/',
        },
        {
          text: 'Novosti',
          disabled: false,
          href: '/novosti',
        },
        {
          text: 'Naziv članka',
          disabled: true,
          href: '',
        },
      ],
    }),
  
    methods: {
      
    }
}
</script>

<style scoped>
.facebook:hover{
    color: #4267B2;
}
.whatsapp:hover{
    color: #25D366;
}
.print:hover{
    color: black;
}.email:hover{
    color: red;
}
</style>