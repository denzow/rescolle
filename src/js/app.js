
import MyComponent from './components/MyComponent.vue';
import Vue from 'vue';

new Vue({
    el: '#app',
    components: {
        MyComponent
    },
    template: '<my-component></my-component>'
});

Vue.component(MyComponent);
