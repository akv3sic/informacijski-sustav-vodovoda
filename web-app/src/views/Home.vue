<template>
    <div>
      <Header/>
      <Hero />
      <FeaturesPresentation />
    </div>
</template>

<script>
import Header from "@/components/layout/TheHeader"
import Hero from "@/components/home/TheHero"
import FeaturesPresentation  from "@/components/home/FeaturesPresentation"

  export default {
    name: 'Home',

    components: {
      Header, Hero, FeaturesPresentation
    },
  }
</script>
