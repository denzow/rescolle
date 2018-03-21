
<template>
    <div class="wrapper">
        <my-header></my-header>
        <my-side-bar></my-side-bar>
        <div class="content-wrapper">
            <my-map-app></my-map-app>
        </div>
    </div>
</template>

<script>
    import MyMapApp from './components/MyMapApp.vue';
    import MyHeader from './components/MyHeader.vue';
    import MySideBar from './components/MySideBar.vue';

    export default {
        name: 'app',
        components: {
            MySideBar,
            MyHeader,
            'my-map-app': MyMapApp,
            'my-header': MyHeader,
            'my-side-bar': MySideBar,

        }
    }
</script>
<style>

</style>