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
  <b-list-group-item href="#" class="flex-column align-items-start">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">List group item heading</h5>
      <h5 @click="addcount( )"><b-badge pill variant="primary">{{count}}</b-badge></h5>
    </div>

    <p class="mb-1">
      Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.
    </p>
    <small>Donec id elit non mi porta.</small><br/><br/>
    <b-button pill size="sm" variant="outline-primary">Download</b-button>
  </b-list-group-item>

  <b-list-group-item href="#" class="flex-column align-items-start">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">List group item heading</h5>
      <small class="text-muted">3 days ago</small>
    </div>

    <p class="mb-1">
      Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.
    </p>

    <small class="text-muted">Donec id elit non mi porta.</small><br/><br/>
    <b-button pill size="sm" variant="outline-secondary">Download</b-button>
  </b-list-group-item>

  <b-list-group-item href="#" class="flex-column align-items-start">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">Disabled List group item</h5>
      <small class="text-muted">3 days ago</small>
    </div>

    <p class="mb-1">
      Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.
    </p>

    <small class="text-muted">Donec id elit non mi porta.</small><br/><br/>
    <b-button pill size="sm" variant="outline-success">Download</b-button>
  </b-list-group-item>
</b-list-group>
    </b-container>
    </div>
</template>
<script>
export default {
  name: 'Data',
  data () {
    return {
      count: 1
    }
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
