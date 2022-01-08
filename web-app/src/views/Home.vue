<template>
    <div>
      <Header/>
      <Hero />
      <FeaturesPresentation />
      <LatestNews />
      <Footer />
    </div>
</template>

<script>
import Header from "@/components/layout/TheHeader"
import Hero from "@/components/home/TheHero"
import FeaturesPresentation  from "@/components/home/FeaturesPresentation"
import LatestNews from '../components/home/LatestNews.vue'
import Footer from "@/components/layout/TheFooter"

  export default {
    name: 'Home',

    components: {
      Header, Hero, FeaturesPresentation, LatestNews, Footer
    },
  }
</script>
