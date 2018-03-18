import MyComponent from './components/MyComponent.vue'
import Vue from 'vue'


new Vue({
    el: '#app',
    components: {
        MyComponent
    }
});

Vue.component(MyComponent);
