<template>
    <div>
      <Header/>
      <Hero />
      <Counters />
      <LatestNews />
      <FeaturesPresentation />
      <Location />
      <Footer />
    </div>
</template>

<script>
import Header from "@/components/layout/TheHeader"
import Hero from "@/components/home/TheHero"
import Counters from "@/components/home/Counters"
import FeaturesPresentation  from "@/components/home/FeaturesPresentation"
import LatestNews from '../components/home/LatestNews.vue'
import Location from '../components/home/Location.vue'
import Footer from "@/components/layout/TheFooter"

  export default {
    name: 'Home',

    components: {
      Header, Hero, Counters, FeaturesPresentation, LatestNews, Footer, Location
    },
  }
</script>
