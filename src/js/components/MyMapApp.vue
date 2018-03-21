<template>
    <div>
        <input type="text" @keyup.enter="search" v-model="keyword"/><input type="button" value="検索" />
        <gmap-map
            ref="map"
            :center="center"
            :zoom="14"
            style="width: 90%; height: 700px">
            <gmap-marker
              :key="index"
              v-for="(m, index) in markers"
              :position="m.position"
              :clickable="true"
              :draggable="false"
              @click="toggleInfoWindow(m, index)">
            </gmap-marker>
            <gmap-info-window :options="infoOptions" :position="infoWindowPos" :opened="infoWinOpen" @closeclick="infoWinOpen=false">
                <my-maker :restaurantInfo="infoContent"></my-maker>
            </gmap-info-window>
        </gmap-map>
    </div>
</template>

<script>
    import Vue from 'vue';
    import * as VueGoogleMaps from 'vue2-google-maps';
    import MyMaker from './MyMaker.vue';
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
        },
        data () {
            return {
                center: {lat: 35.658581, lng: 139.745433},
                markers: [],
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
                search: function(){
                    const map = this.$refs.map.$mapObject;
                    const bounds = map.getBounds();
                    console.log(map.getBounds());
                    const data = {
                        'keyword': this.keyword,
                        'north_east_lat': bounds.getNorthEast().lat(),
                        'north_east_lng': bounds.getNorthEast().lng(),
                        'south_west_lat': bounds.getSouthWest().lat(),
                        'south_west_lng': bounds.getSouthWest().lng(),
                    };

                    this.markers = [];
                    fetch('/get_coordinate_list', {
                        method: 'POST',
                        mode: 'same-origin',
                        credentials: 'include',
                        headers: {
                            'X-CSRFToken': getCookie('csrftoken'),
                            'Accept': 'application/json',
                        },
                        body: generateFormData(data)
                    })
                    .then(res => {
                        return res.json();
                    })
                    .then(json => {

                        for (let rest of json['restaurants']) {
                            this.markers.push({
                                position: {
                                    lat: rest['latitude'],
                                    lng: rest['longitude'],
                                },
                                restaurantId: rest['id'],
                            })
                        }
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
                    console.log(this.infoContent);
                }
            }
        },
    }


</script>
<style>

</style>