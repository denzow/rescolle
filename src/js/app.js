import App from './App.vue';
import Vue from 'vue';
import store from './store';

import 'va/lib/css'
import 'va/lib/script'


new Vue({
  store,
  el: '#app',
  components: {
    App
  },
  template: '<app></app>'
});

Vue.component(App);
