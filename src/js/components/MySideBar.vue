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
      <!-- /.search form -->
      <!-- sidebar menu: : style can be found in sidebar.less -->
      <ul class="sidebar-menu tree" data-widget="tree">
        <li class="header">コレクションリスト</li>
        <li class="active treeview menu-open">
          <a href="#">
            <i class="fa fa-folder"></i> <span>れすこれリスト</span>
            <span class="pull-right-container">
              <i class="fa fa-angle-left pull-right"></i>
            </span>
          </a>
          <ul class="treeview-menu">
            <li><a href="index.html"><i class="fa fa-cutlery"></i> 牛角 </a></li>
            <li class="active"><a href="index2.html"><i class="fa fa-cutlery"></i>ハンバーガー</a></li>
          </ul>
        </li>
        <li class="treeview">
          <a href="#">
            <i class="fa fa-folder"></i> <span>れすこれリスト</span>
            <span class="pull-right-container">
              <i class="fa fa-angle-left pull-right"></i>
            </span>
          </a>
          <ul class="treeview-menu">
            <li><a href="index.html"><i class="fa fa-circle-o"></i> 牛角 </a></li>
            <li class="active"><a href="index2.html"><i class="fa fa-circle-o"></i>ハンバーガー</a></li>
          </ul>
        </li>
      </ul>
    </section>
    <!-- /.sidebar -->
  </aside>
</template>

<script>

    import EventBus from '../eventbus/EventBus';

    export default {
        name: 'MySideBar',
        created() {
            EventBus.$on('search-restaurant-end', (data)=>{
                this.isDisabled = false;
                this.searchMessage = 'Search...'
            });
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
        }
    }
</script>