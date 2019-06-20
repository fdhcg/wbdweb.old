<template>
    <div class="docs">
    <b-container >
 <b-list-group >
  <b-list-group-item href="#" class="flex-column align-items-start">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">List group item heading</h5>
      <small>3 days ago</small>
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
  name: 'Data'
}
</script>
<style>
.docs{
  margin-top: 80px;
}
</style>
