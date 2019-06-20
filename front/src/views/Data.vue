<template>
    <div class="data">
      <br/><br/>
       <b-jumbotron bg-variant="secondary" text-variant="white" border-variant="dark">
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
    <b-row>
      <b-col lg="4">
        <b-input-group>
          <b-form-input v-model="keyword_" placeholder="search" ></b-form-input>
          <b-input-group-append>
            <b-button variant="dark"  @click="search()">search</b-button>
          </b-input-group-append>
        </b-input-group>
      </b-col>
    </b-row>
  </b-jumbotron>

    <b-container>
      <b-row v-if="keyword !== '*'">
      <span style="float:center-buttom; margin-left: 20px;margin-top:4px">keyword: {{keyword}}</span><b-btn variant="light" size="sm" style="margin-left: 20px" @click="erease()">erease</b-btn>
      </b-row>
 <b-list-group style="margin-top: 20px">
   <b-list-group-item v-if="checkEmpty(data_list)">
      <span>Nothing found!</span>
  </b-list-group-item>
  <b-list-group-item v-for="item in data_list" :key="item.title" href="#" class="flex-column align-items-start">
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
import {isEmpty} from '../components/common.js'
export default {
  name: 'Data',
  data () {
    return {
      backendUrl: ' ',
      keyword: '',
      keyword_: '',
      data_list: ''
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
    },
    checkEmpty (obj) {
      return isEmpty(obj)
    },
    makeToast (append = false) {
      this.$bvToast.toast(`尚未输入关键字！`, {
        title: '未进行搜索',
        autoHideDelay: 5000,
        appendToast: append
      })
    },
    update_key () {
      this.keyword = this.keyword_
      this.COMMON.keyword = this.keyword
      this.keyword_ = ''
    },
    search () {
      if (this.keyword_ !== '') {
        this.update_key()
        axios.post(this.backendUrl + '/pull_data', {'target': this.keyword}).then(response => (this.data_list = response.data))
      } else {
        this.makeToast()
        window.location.assign('#')
      }
    },
    erease () {
      this.COMMON.keyword = '*'
      this.keyword = '*'
      axios.post(this.backendUrl + '/pull_data', {'target': this.keyword}).then(response => (this.data_list = response.data))
    }
  }
}
</script>
<style>
</style>
