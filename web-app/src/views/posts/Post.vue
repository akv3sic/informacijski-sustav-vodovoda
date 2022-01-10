<template>
    <div>
        <Header />
        <v-container
            :class="{'pa-16':$vuetify.breakpoint.mdAndUp}"
        >
            <v-breadcrumbs :items="breadcrumbsItems"></v-breadcrumbs>
            <h2 class="display-1 pl-5 pb-2">Naslov članka</h2>
            <v-row class="pl-5">
                <v-col md="4" cols="12">
                    <v-icon class="mx-1" color="primary">mdi-account</v-icon>
                    <p class="body-2 d-inline grey--text">Ante Kvesić</p>
                </v-col>
                <v-col md="4" cols="12">
                    <v-icon class="mx-1" color="primary">mdi-calendar</v-icon>
                    <p class="body-2 d-inline grey--text">3.1.2022.</p>
                </v-col>
            </v-row>
            <v-row class="px-8">
                <v-col>
                    <v-img 
                        src="http://www.mz-kocerin.ba/wp-content/uploads/2016/02/Odluku-o-naplati-neizmirenih-obaveza-prema-Udruzi-800x445.jpg"
                        cover
                        max-height="500px"
                    >
                    </v-img>  
                </v-col>

            </v-row>
            <v-row class="pl-5">
                <v-col>
                    <div class="my-3">
                        <v-icon class="mx-1 facebook">mdi-facebook</v-icon>
                        <v-icon class="mx-1 whatsapp">mdi-whatsapp</v-icon>
                        <v-icon class="mx-1 print">mdi-printer</v-icon>
                        <v-icon class="mx-1 email">mdi-email</v-icon>
                    </div>
                        <p class="mt-3">
                            Adipiscing elit duis tristique sollicitudin nibh. Sed faucibus turpis in eu mi bibendum. Viverra orci sagittis eu volutpat odio facilisis mauris sit amet. Eu non diam phasellus vestibulum lorem sed. Maecenas volutpat blandit aliquam etiam erat velit.
                            Adipiscing elit duis tristique sollicitudin nibh. Sed faucibus turpis in eu mi bibendum. Viverra orci sagittis eu volutpat odio facilisis mauris sit amet. Eu non diam phasellus vestibulum lorem sed. Maecenas volutpat blandit aliquam etiam erat velit.
                            Adipiscing elit duis tristique sollicitudin nibh. Sed faucibus turpis in eu mi bibendum. Viverra orci sagittis eu volutpat odio facilisis mauris sit amet. Eu non diam phasellus vestibulum lorem sed. Maecenas volutpat blandit aliquam etiam erat velit.
                        </p>
                        <p class="grey--text">
                            Objavljeno: 4.1.2022. 15:33:59
                        </p>
                </v-col>
            </v-row>

        </v-container>
        <Footer />
    </div>
</template>

<script>
import Header from '../../components/layout/TheHeader.vue'
import Footer from '../../components/layout/TheFooter.vue'
export default {
    name: "Post",
    components: { Header, Footer },
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
    color: #CA2621;
}
</style>