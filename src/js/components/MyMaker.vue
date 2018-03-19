<template>
    <div>
        <h3>{{restaurantInfo.name}}</h3>
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