<template>
    <div>
        <input type="text" @keyup.enter="search" v-model="keyword"/><input type="button" value="検索" />
        <gmap-map
            :center="center"
            :zoom="14"
            style="width: 500px; height: 300px">
            <gmap-marker
              :key="index"
              v-for="(m, index) in markers"
              :position="m.position"
              :clickable="true"
              :draggable="false"
              @click="toggleInfoWindow(m, index)">
            </gmap-marker>
            <gmap-info-window :options="infoOptions" :position="infoWindowPos" :opened="infoWinOpen" @closeclick="infoWinOpen=false">
            {{infoContent}}
            </gmap-info-window>
        </gmap-map>
    </div>
</template>

<script>
    import * as VueGoogleMaps from 'vue2-google-maps';
    import Vue from 'vue';

    Vue.use(VueGoogleMaps, {
        load: {
            key: '',
            v: '',
        }
    });

    export default {
        data () {
            return {
                center: {lat: 35.658581, lng: 139.745433},
                markers: [
                    {
                        position: {lat: 35.658581, lng: 139.745433},
                        infoText: 'test1'
                    },
                    {
                        position: {lat: 35.659581, lng: 139.745433},
                        infoText: 'test2'
                    }
                ],
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
                    let keyWord = this.keyword;
                    console.log(keyWord);
                    this.markers = [];
                    fetch('/get_coordinate_list?keyword=' + keyWord, {
                        method: 'GET',
                        mode: 'same-origin',
                        credentials: 'include'
                    })
                    .then(res => {
                        return res.json();
                    })
                    .then(json => {
                        let center = json['center'];
                        if(center['latitude'] === null){
                            return
                        }
                        this.center = {
                            lat: center['latitude'],
                            lng: center['longitude']
                        };

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
                    this.infoContent = JSON.stringify(restaurantInfo);
                }
            }
        },
    }


</script>
<style>

</style>