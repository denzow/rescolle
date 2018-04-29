<template>
    <div>
        <gmap-map
                ref="map"
                :center="center"
                :zoom="14"
                @click="closeInfoWindow"
                style="width: 90%; height: 700px">
            <gmap-marker
                    :key="`search_${index}`"
                    v-for="(m, index) in markers"
                    :position="m.position"
                    :clickable="true"
                    :draggable="false"
                    @click="toggleInfoWindow(m, index)">
            </gmap-marker>

            <gmap-marker
                    :key="`cl_${index}`"
                    v-for="(m, index) in collectedMarkers"
                    :position="m.position"
                    :clickable="true"
                    :draggable="false"
                    :icon="{'url': 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'}"
                    @click="toggleInfoWindow(m, index)">
            </gmap-marker>

            <gmap-info-window
                    :options="infoOptions"
                    :position="infoWindowPos"
                    :opened="infoWinOpen"
                    @closeclick="closeInfoWindow">
                <my-maker :restaurantInfo="infoContent"></my-maker>
            </gmap-info-window>
        </gmap-map>
        <restaurant-menu :restaurantInfo="infoContent"></restaurant-menu>
    </div>
</template>

<script>
  import EventBus from '../eventbus/EventBus';
  import Vue from 'vue';
  import ClickOutside from 'vue-click-outside';
  import * as VueGoogleMaps from 'vue2-google-maps';
  import MyMaker from './MyMaker.vue';
  import RestaurantMenu from './RestaurantMenu.vue';
  import {
    getCookie,
    generateFormData,
  } from '../lib/utils';


  Vue.use(VueGoogleMaps, {
    load: {
      key: '',
      v: '',
    }
  });
  export default {
    components: {
      'my-maker': MyMaker,
      'restaurant-menu': RestaurantMenu,
    },
    directives: {
      ClickOutside
    },
    created() {
      EventBus.$on('search-restaurant', (data) => {
        this.search(data.keyword);
      });
    },
    data() {
      return {
        center: {lat: 35.658581, lng: 139.745433},
        currentMidx: null,
        infoWinOpen: false,
        infoContent: '',
        infoOptions: {
          pixelOffset: {
            width: 0,
            height: -35
          }
        },
        infoWindowPos: {
          lat: 0,
          lng: 0
        },
        keyword: '',
      }
    },
    computed: {
      markers: function () {
        return this.$store.state.markers;
      },
      collectedMarkers: function () {
        return this.$store.state.collectedMarkers;
      }
    },
    methods: {
      search: function (keyword) {
        this.keyword = keyword;
        const map = this.$refs.map.$mapObject;
        const bounds = map.getBounds();
        const data = {
          'keyword': keyword,
          'north_east_lat': bounds.getNorthEast().lat(),
          'north_east_lng': bounds.getNorthEast().lng(),
          'south_west_lat': bounds.getSouthWest().lat(),
          'south_west_lng': bounds.getSouthWest().lng(),
        };
        this.$store.dispatch('search', data).then(d => {
          EventBus.$emit('search-restaurant-end');
        });

      },
      toggleInfoWindow: async function (marker, idx) {
        this.infoWindowPos = marker.position;

        //check if its the same marker that was selected if yes toggle
        if (this.currentMidx === idx) {
          this.infoWinOpen = !this.infoWinOpen;
        }
        //if different marker set infowindow to open and reset current marker index
        else {
          this.infoWinOpen = true;
          this.currentMidx = idx;
        }
        let restaurantInfo = await fetch('/get_restaurant/' + marker.restaurantId, {
          method: 'GET',
          mode: 'same-origin',
          credentials: 'include'
        })
          .then(res => {
            return res.json();
          });
        this.infoContent = restaurantInfo['restaurant'];
      },
      closeInfoWindow() {
        this.infoWinOpen = false;
      }
    }
  }


</script>
<style>

</style>