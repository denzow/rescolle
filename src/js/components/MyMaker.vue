<template>
  <div class="restaurant-info-window">
    <h3>{{restaurantInfo.name}}</h3>
    <div style="display:flex">
            <span v-for="(image_url, index) in restaurantInfo.image_url_list">
                <a :href="image_url" target="_blank">
                    <img class="thumbnail" :src="image_url"/>
                </a>
            </span>
    </div>
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
<style scoped>
  .thumbnail {
    width: 100px;
  }

  .restaurant-info-window {
    max-width: 600px;
    max-height: 400px;
  }
</style>