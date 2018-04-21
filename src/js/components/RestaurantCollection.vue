<template>
    <li class="active treeview">
      <a href="#">
        <i class="fa fa-folder"></i> <span>{{ collection.name }}</span>
        <span class="pull-right-container">
          <i class="fa fa-angle-left pull-right"></i>
        </span>
      </a>
      <ul class="treeview-menu"  style="display: none">
        <li v-for="(restaurant, index) in restaurantList" :key="restaurant.id" class="collected-restaurant">
          <a href="#" >
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
      restaurantList(){
        console.log(this.collection);
        return this.collection.restaurants;
      }
    }
  }
</script>
<style scoped>
  .collected-restaurant {
    width: 100px;
    overflow-wrap: break-word;
  }
</style>