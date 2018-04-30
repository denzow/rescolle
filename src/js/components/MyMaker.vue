<template>
  <div class="restaurant-info-window">
    <div class="tool-bar">
      <div>
        <span class="add-collection-box" @click="showAddMenu">
          <span class="fa fa-folder-open"></span>
          add collection
        </span>
        <div v-show="showMenu" class="add-collection-menu">
          <select @change="setSelectedCollection">
            <option v-for="collection in getCollectionListForSelect"
                    :key="collection.id"
                    :value="collection.id">
              {{ collection.name }}
            </option>
          </select>
          <button type="button" @click="addCollectionRequest">ADD</button>
        </div>
      </div>
    </div>
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
  import { mapActions, mapGetters } from 'vuex';

  export default {
    props: [
      'restaurantInfo',
    ],
    computed:{
      restaurantId() {
        return this.restaurantInfo.id;
      },
      ...mapGetters(['getCollectionListForSelect'])
    },
    methods: {
      setSelectedCollection(event) {
        this.selectedCollectionId = parseInt(event.target.value);
      },
      showAddMenu() {
        this.showMenu = !this.showMenu;
      },
      addCollectionRequest() {
        console.log('addCollectionRequest', this.selectedCollectionId);
        if(this.selectedCollectionId === null){
          return;
        }
        this.addCollection({
          restaurantId: this.restaurantId,
          collectionId: this.selectedCollectionId,
          memo: 'n/a',
        });
      },
      ...mapActions(['addCollection']),
    },
    data() {
      return {
        showMenu: false,
        selectedCollectionId: null,
      };
    },
  }
</script>
<style scoped lang="scss">
  .thumbnail {
    width: 100px;
  }

  .restaurant-info-window {
    max-width: 600px;
    max-height: 400px;
  }

  .tool-bar {
    display: flex;
    flex-direction: row-reverse;
    padding: 5px;
  }

  .add-collection-box {
    border: solid 1px;
    border-radius: 5px;
    padding: 2px;
    background-color: #EEEEEE;
    color: #333333;
    cursor: pointer;
    &:hover {
      color: #EEEEEE;
      background-color: #333333;
    }
  }

  .add-collection-menu {
    background-color: #FFFFFF;
    padding: 5px;
  }
</style>