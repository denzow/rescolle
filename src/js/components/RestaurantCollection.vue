<template>
  <li class="treeview" @click="setCollectionToMark">
    <a href="#">
      <i class="fa fa-folder"></i> <span>{{ collection.name }}</span>
      <span class="pull-right-container">
        <i class="fa fa-angle-left pull-right"></i>
      </span>
    </a>
    <ul class="treeview-menu">
      <li v-for="(restaurant, index) in restaurantList" :key="restaurant.id" class="collected-restaurant">
        <a href="#">
          <i class="fa fa-cutlery"></i>{{ restaurant.restaurant_name }}
        </a>
      </li>
    </ul>
  </li>
</template>
<script>
  export default {
    props: [
      'collection',
    ],
    computed:{
      restaurantList() {
        console.log(this.collection.id);
        return this.collection.restaurants;
      }
    },
    methods:{
      setCollectionToMark() {
        console.log('setCollectionToMark');
        this.$store.dispatch('setCollectionToMark', {
          collectionId: this.collection.id
        });
      },
    },
  }
</script>
<style scoped>
  .collected-restaurant {
    width: 100px;
    overflow-wrap: break-word;
  }
</style>