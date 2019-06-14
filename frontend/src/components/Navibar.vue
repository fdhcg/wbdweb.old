<template>
<div>
  <b-navbar toggleable="lg" type="dark" variant="dark" fixed="top">
    <b-navbar-brand href="#/">WBD</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item v-for="item in navitem" :key="item.name"  v-bind:href="'#'+item.url" >{{item.name}}</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit" variant="outline-light">Search</b-button>
        </b-nav-form>

        <b-nav-item-dropdown text="Lang" right>
          <b-dropdown-item href="#">EN</b-dropdown-item>
          <b-dropdown-item href="#">ES</b-dropdown-item>
          <b-dropdown-item href="#">RU</b-dropdown-item>
          <b-dropdown-item href="#">FA</b-dropdown-item>
        </b-nav-item-dropdown>

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template slot="button-content"><em>User</em></template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item href="#">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
<!--<div id="navibar-con" class="col-md-12">
  <nav v-bind:class="active" >
    <router-link to="/" class="home" @mouseover.native="makeActive('home')">home</router-link>
    <router-link v-for="item in navitem" :key="item.name"  v-bind:to="item.url" :class=item.name @mouseover.native="makeActive(item.name)">{{item.name}}</router-link>
  </nav>
</div>-->
</template>
<script>
/* eslint-disable */
export default {
  name: 'Navibar',
  data () {
    return {
      active: 'home',
      navitem: [{name: 'home',url: '/'},{name: 'data',url: '/data'},
      {name: 'research',url: '/research'},{name: 'docs',url: '/docs'},
      {name: 'zeppelin',url: '/zeppelin'},{name: 'about',url: '/about'}]
    }
  },
  methods:{
    makeActive: function (item) {
    this.active = item
    }
  }
}
</script>
<style>
</style>
