import Vue from 'vue';
import Vuex from 'vuex';

import {
  getJson,
  postJson,
} from '../lib/utils';


Vue.use(Vuex);


const state = {
  searchWord: '',
  markers: [],
  collectedMarkers: [],
  collectionList: [],
};

const getters = {
  getCollectionListForSelect(state, getters) {
    return state.collectionList.map(collection => {
      return {
        id: collection.id,
        name: collection.name,
      }
    })
  },
};

const actions = {
  async addCollection(context, payload){
    await postJson('add_restaurant_to_collection/', {
      collection_id: payload.collectionId,
      restaurant_id: payload.restaurantId,
      memo: payload.memo,
    }, 'json');

    context.dispatch('initCollection');
  },
  setMarkers(context, payload) {
    context.commit('setMarkers', payload);
  },
  search(context, payload) {
    let markers = [];
    postJson('/get_coordinate_list', payload)
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
  setSearchWord(context, payload) {
    context.commit('setSearchWord', payload)
  },
  initCollection(context){
    console.log('initCollection');
    getJson('/get_collection_list')
      .then(json => {
        context.commit('setCollection', json)
      });
  },
  setCollectionToMark(context, payload){
    const collectionId = payload.collectionId;
    const markers = [];
    getJson(`/get_coordinate_list/${collectionId}`)
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
        context.commit('setCollectedMarkers', {markers});
      });
  }
};
const mutations = {
  setMarkers(state, payload) {
    state.markers = payload.markers;
  },
  setSearchWord(state, payload) {
    state.searchWord = payload.searchWord;
  },
  setCollection(state, payload) {
    state.collectionList = payload.collection_list;
  },
  setCollectedMarkers(state, payload){
    state.collectedMarkers = payload.markers;
  }
};


export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations,
});
