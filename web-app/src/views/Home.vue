<template>
    <div>
      <Header/>
      <Hero />
    </div>
</template>

<script>
import Header from "@/components/layout/TheHeader"
import Hero from "@/components/home/TheHero"

  export default {
    name: 'Home',

    components: {
      Header, Hero
    },
  }
</script>
