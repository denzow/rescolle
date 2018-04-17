
import App from './App.vue';
import Vue from 'vue';
import Vuex from 'vuex';
import 'va/lib/css'
import 'va/lib/script'
import {
    getCookie,
    generateFormData,
} from './lib/utils';


Vue.use(Vuex);


const store = new Vuex.Store({
    state: {
        searchWord: '',
        markers: [],
    },
    actions: {
        setMarkers(context, payload){
            context.commit('setMarkers', payload);
        },
        search(context, payload){
            let markers = [];

            fetch('/get_coordinate_list', {
                method: 'POST',
                mode: 'same-origin',
                credentials: 'include',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Accept': 'application/json',
                },
                body: generateFormData(payload)
            })
            .then(res => {
                return res.json();
            })
            .then(json => {

                for (let rest of json['restaurants']) {
                    markers.push({
                        position: {
                            lat: rest['latitude'],
                            lng: rest['longitude'],
                        },
                        restaurantId: rest['id'],
                    })
                }
                context.commit('setMarkers', {markers})
            });
        },
        setSearchWord(context, payload){
            context.commit('setSearchWord', payload)
        }
    },
    mutations: {
        setMarkers(state, payload){
            state.markers = payload.markers;
        },
        setSearchWord(state, payload){
            state.searchWord = payload.searchWord;
        }
    },
});

new Vue({
    store,
    el: '#app',
    components: {
        App
    },
    template: '<app></app>'
});

Vue.component(App);
