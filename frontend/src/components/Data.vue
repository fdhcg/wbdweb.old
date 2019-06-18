<template>
    <div class="data">
      <br/><br/>
       <b-jumbotron bg-variant="secondary" text-variant="white" border-variant="warning">
    <template slot="header">BootstrapVue</template>

    <template slot="lead">
      This is a simple hero unit, a simple jumbotron-style component for calling extra attention to
      featured content or information.
    </template>

    <hr class="my-4">

    <p>
      It uses utility classes for typography and spacing to space content out within the larger
      container.
    </p>

    <b-button variant="primary" href="#">Do Something</b-button>
    <b-button variant="success" href="#">Do Something Else</b-button>
  </b-jumbotron>
    <b-container >
 <b-list-group >
  <b-list-group-item v-for="item in data_list" :key="item" href="#" class="flex-column align-items-start">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">{{item.title}}</h5>
      <small class="text-muted">3 days ago</small>
    </div>
    <p>origin={{item.origin}}</p>
    <b-button pill size="sm" variant="outline-success">Download</b-button>
  </b-list-group-item>
</b-list-group>
    </b-container>
    </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'Data',
  data () {
    return {
      backendUrl: ' ',
      keyword: ' ',
      data_list: ' '
    }
  },
  mounted: function () {
    this.$nextTick(function () {
      this.backendUrl = this.COMMON.url + ':8000/api'
      this.keyword = this.COMMON.keyword

      axios.post(this.backendUrl + '/pull_data', {'target': this.keyword}).then(response => (this.data_list = response.data))
    })
  },
  methods: {
    addcount () {
      this.count += 1
    }
  }
}
</script>
<style>
</style>
