
import MyMapApp from './components/MyMapApp.vue';
import Vue from 'vue';

new Vue({
    el: '#app',
    components: {
        MyMapApp
    },
    template: '<my-map-app></my-map-app>'
});

Vue.component(MyMapApp);
