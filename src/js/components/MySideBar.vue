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
        <li class="header">MAIN NAVIGATION</li>
        <li class="active treeview menu-open">
          <a href="#">
            <i class="fa fa-dashboard"></i> <span>Dashboard</span>
            <span class="pull-right-container">
              <i class="fa fa-angle-left pull-right"></i>
            </span>
          </a>
          <ul class="treeview-menu">
            <li><a href="index.html"><i class="fa fa-circle-o"></i> Dashboard v1</a></li>
            <li class="active"><a href="index2.html"><i class="fa fa-circle-o"></i> Dashboard v2</a></li>
          </ul>
        </li>
        <li class="treeview">
          <a href="#">
            <i class="fa fa-files-o"></i>
            <span>Layout Options</span>
            <span class="pull-right-container">
              <span class="label label-primary pull-right">4</span>
            </span>
          </a>
          <ul class="treeview-menu">
            <li><a href="pages/layout/top-nav.html"><i class="fa fa-circle-o"></i> Top Navigation</a></li>
            <li><a href="pages/layout/boxed.html"><i class="fa fa-circle-o"></i> Boxed</a></li>
            <li><a href="pages/layout/fixed.html"><i class="fa fa-circle-o"></i> Fixed</a></li>
            <li><a href="pages/layout/collapsed-sidebar.html"><i class="fa fa-circle-o"></i> Collapsed Sidebar</a></li>
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
        searchMessage: 'Search...',
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
                search: function(){
                    console.log(this.searchWord);
                    this.isDisabled = true;
                    this.searchMessage = 'Searching.'
                    EventBus.$emit('search-restaurant', {'keyword': this.searchWord})
                },
            }
        }
    }
</script>