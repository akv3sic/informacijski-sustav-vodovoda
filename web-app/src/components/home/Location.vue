<template>              
    <v-container fluid grey lighten-4 class="mt-10">
      <v-row class="">

        <GmapMap
        :center="position"
        :zoom="17"
        map-type-id="terrain"
        style="width: 100%; height: 45vh"
        >
          <GmapMarker
            :position="position"
            :clickable="true"
            :draggable="true"
        />
        </GmapMap>

      </v-row>
    </v-container>
</template>


<script>
import Vue from 'vue'
import * as VueGoogleMaps from 'vue2-google-maps'
 
Vue.use(VueGoogleMaps, {
  load: {
    key: process.env.VUE_APP_GMAPS_API_KEY,
    libraries: 'places', // This is required if you use the Autocomplete plugin
    // OR: libraries: 'places,drawing'
    // OR: libraries: 'places,drawing,visualization'
    // (as you require)
 
    //// If you want to set the version, you can do so:
    // v: '3.26',
  },
 
  //// If you intend to programmatically custom event listener code
  //// (e.g. `this.$refs.gmap.$on('zoom_changed', someFunc)`)
  //// instead of going through Vue templates (e.g. `<GmapMap @zoom_changed="someFunc">`)
  //// you might need to turn this on.
  // autobindAllEvents: false,
 
  //// If you want to manually install components, e.g.
  //// import {GmapMarker} from 'vue2-google-maps/src/components/marker'
  //// Vue.component('GmapMarker', GmapMarker)
  //// then disable the following:
  // installComponents: true,
})


export default {
    name: "Location",
    data: () => ({
      position: { lat: Number(43.34574821306392), lng: Number(17.796667099997762) } 
    }),
      mounted: function () {
    // `this` points to the vm instance
    console.log(process.env)
  }
}
</script>