<template>
    <div>
      <Header/>
      <Hero />
      <FeaturesPresentation />
      <LatestNews />
    </div>
</template>

<script>
import Header from "@/components/layout/TheHeader"
import Hero from "@/components/home/TheHero"
import FeaturesPresentation  from "@/components/home/FeaturesPresentation"
import LatestNews from '../components/home/LatestNews.vue'

  export default {
    name: 'Home',

    components: {
      Header, Hero, FeaturesPresentation, LatestNews
    },
  }
</script>
