<template>
    <div>
        <h3>{{restaurantInfo.name}}</h3>
        <div>
            <a v-if="restaurantInfo.gnavi_url" :href="restaurantInfo.gnavi_url" target="_blank">
                <img src="https://r.gnavi.co.jp/favicon.ico" style="width:25px;"/>
            </a>
        </div>
        <div v-html="restaurantInfo.description"></div>
        <div>
            {{restaurantInfo.address}}
            {{restaurantInfo.tel}}
        </div>
    </div>
</template>
<script>
    export default {
        props: [
            'restaurantInfo',
        ],
    }
</script>
<style>

</style>