<template>
  <aside class="main-sidebar">
    <!-- sidebar: style can be found in sidebar.less -->
    <section class="sidebar" style="height: auto;">
      <!-- search form -->
      <form action="#" method="get" class="sidebar-form" v-on:submit.prevent="search">
        <div class="input-group">
          <input type="text" name="q" class="form-control" :placeholder="searchMessage" v-model="searchWord" :disabled="isDisabled">
          <span class="input-group-btn">
                <button name="search" type="submit" id="search-btn" class="btn btn-flat" :disabled="isDisabled">
                  <i class="fa fa-search"></i>
                </button>
          </span>
        </div>
      </form>
      <ul class="sidebar-menu tree" data-widget="tree">
        <li class="header">コレクションリスト</li>
        <restaurant-collection v-for="(collection, index) in collectionList" :collection="collection"/>
      </ul>
    </section>
    <!-- /.sidebar -->
  </aside>
</template>

<script>

  import EventBus from '../eventbus/EventBus';
  import RestaurantCollection from './RestaurantCollection.vue';

  export default {
    name: 'MySideBar',
    created() {
      EventBus.$on('search-restaurant-end', (data)=>{
        this.isDisabled = false;
        this.searchMessage = 'Search...'
      });
      this.$store.dispatch('initCollection');
    },
    components:{
      RestaurantCollection
    },
    data() {
      return {
        isDisabled: false,
        searchWord: '',
        searchMessage: 'Search...',
        search: function(){
          console.log(this.searchWord);
          this.isDisabled = true;
          this.searchMessage = 'Searching.';
          EventBus.$emit('search-restaurant', {'keyword': this.searchWord})
        },
      }
    },
    computed: {
      collectionList(){
          return this.$store.state.collectionList;
      }
    },
  }
</script>