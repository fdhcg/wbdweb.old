<template>
  <div id="app">
        <b-container class="bv-example-row bv-example-row-flex-cols headline">
          <b-row>
           <b-col offse-md="1" md="6" order-sm="1" class="d-none d-sm-block">
              <div class="banner">
              </div>
            </b-col>
            <b-col md="5" order-sm="2">
              <b-jumbotron  bg-variant="light" text-variant="dark" border-variant="light">
                <template slot="header">WBD</template>
                <template slot="lead">{{label1}}
                    search for data?
                </template>
                <hr class="my-4">
                <b-input-group>
                    <b-form-input v-model="keyword" placeholder="search" ></b-form-input>
                    <b-input-group-append>
                      <b-button variant="secondary"  @click="search()">search</b-button>
                      </b-input-group-append>
                    </b-input-group>
                </b-jumbotron>
              </b-col>
          </b-row>
          <br/><br/>
        </b-container>
        <transition name="fade">
      <div v-show=flag1 key="pic">
        <b-container>
          <b-row style="font-size: 20px">
            <b-col cols="6">
            <div><h2>Request Data About Wireless Big Data?</h2></div>
            <div><br/>Not finding the right data?<br/> We can get it for you</div>
            <div>
              <b-btn href="#" size="sm" variant="dark">Request Data</b-btn>
            </div>
            </b-col>
            <b-col cols="6">
              <b-row>
                <img src="../assets/sec4-4.png" alt="attr2" width="25" height="25" hspace="20" vspace="30">
                <div>
                  <h3>some brief </h3>
                  some brief introduction about attr2
                  </div>
              </b-row>
              <b-row>
                <img src="../assets/sec4-2.png" alt="attr2" width="25" height="25" hspace="20" vspace="30">
                <div>
                  <h3>some brief </h3>
                 some brief introduction about attr2
                </div>
              </b-row>
              <b-row>
                <img src="../assets/sec4-1.png" alt="attr2" width="25" height="25" hspace="20" vspace="30">
                <div>
                  <h3>some brief </h3>
                  some brief introduction about attr2
                </div>
              </b-row>
            </b-col>
          </b-row>
          <!-- <b-row style="font-size: 20pxp; margin-top: 20px">
            <b-col cols="6">
              <b-row>
                <img src="../assets/sec4-4.png" alt="attr2" width="25" height="25" hspace="20" vspace="30">
                <div>
                  <h3>some brief </h3>
                  some brief introduction about attr2
                  </div>
              </b-row>
              <b-row>
                <img src="../assets/sec4-2.png" alt="attr2" width="25" height="25" hspace="20" vspace="30">
                <div>
                  <h3>some brief </h3>
                 some brief introduction about attr2
                </div>
              </b-row>
              <b-row>
                <img src="../assets/sec4-1.png" alt="attr2" width="25" height="25" hspace="20" vspace="30">
                <div>
                  <h3>some brief </h3>
                  some brief introduction about attr2
                </div>
              </b-row>
            </b-col>
            <b-col cols="6">
            <div><h2>Request Data About Wireless Big Data?</h2></div>
            <div><br/>Not finding the right data?<br/> We can get it for you</div>
            <div>
              <b-btn href="#" size="sm" variant="dark">Request Data</b-btn>
            </div>
            </b-col>
          </b-row> -->
          <!-- <div class="text-center">
           <b-spinner label="Spinning"></b-spinner>
           <b-spinner type="grow" label="Spinning"></b-spinner>
           <b-spinner variant="primary" label="Spinning"></b-spinner>
           <b-spinner variant="primary" type="grow" label="Spinning"></b-spinner>
           <b-spinner variant="success" label="Spinning"></b-spinner>
           <b-spinner variant="success" type="grow" label="Spinning"></b-spinner>
          </div> -->
        </b-container>
        </div>
          </transition>
          <div data-wow-delay="0.5s" style="margin-top: 50px">
          <div class="intro1 wow slideInLeft">
            <div><h1>WBD</h1></div>
          </div>
           <div class="intro2 wow slideInRight">
            <h1>WBD</h1>
           </div>
            <div class="intro3 wow slideInLeft">
            <h1>WBD</h1>
            </div>
            <div class="intro-end">
            </div>
          </div>
          <!-- <div class="endblock">
            <b-container>
              <b-row >
                <b-col cols="12">
          <b-list-group>
            <b-list-group-item href="#" class="flex-column align-items-start">
              <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">List group item heading</h5>
                <small>3 days ago</small>
              </div>
              <small>Donec id elit non mi porta.</small><br/><br/>
              <b-button pill size="sm" variant="outline-success">Download</b-button>
       <b-button style="float:right" id="popover-1" variant="primary">Using properties</b-button>
        <b-popover
          target="popover-1"
          title="Prop Examples"
          triggers="hover focus"
          content="Embedding content using properties is easy"
        ></b-popover>
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
       <b-button style="float:right" id="popover-2" variant="primary">Using properties</b-button>
        <b-popover
          target="popover-2"
          title="Prop Examples"
          triggers="hover focus"
          content="Embedding content using properties is easy"
        ></b-popover>
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
       <b-button style="float:right" id="popover-2" variant="primary">Using properties</b-button>
        <b-popover
          target="popover-2"
          title="Prop Examples"
          triggers="hover focus"
          content="Embedding content using properties is easy"
        ></b-popover>
  </b-list-group-item>
            <b-list-group-item href="#" class="flex-column align-items-start">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">Disabled List group item</h5>
      <small @click="add_label()" class="text-muted">{{label1}}</small>
    </div>

    <p class="mb-1">
      Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.
    </p>

    <small class="text-muted">Donec id elit non mi porta.</small><br/><br/>
    <b-button pill size="sm" variant="outline-success">Download</b-button>
       <b-button style="float:right" id="popover-2" variant="primary">Using properties</b-button>
        <b-popover
          target="popover-2"
          title="Prop Examples"
          triggers="hover focus"
          content="Embedding content using properties is easy"
        ></b-popover>
  </b-list-group-item>
          </b-list-group>
                </b-col>
              </b-row>
        </b-container>
          </div> -->
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'App',
  data () {
    return {
      flag1: false,
      label1: 1,
      backendUrl: '',
      keyword: ''
    }
  },
  mounted: function () {
    this.$nextTick(function () {
      this.flag1 = true
      this.backendUrl = this.COMMON.url
      axios.get(this.backendUrl + '/api/show_label').then(response => (this.label1 = response.data.label1))
    })
  },
  methods: {
    makeToast (append = false) {
      this.$bvToast.toast(`尚未输入关键字！`, {
        title: '无搜索结果',
        autoHideDelay: 5000,
        appendToast: append
      })
    },
    updateKey () {
      this.COMMON.keyword = this.keyword
    },
    search () {
      if (this.keyword !== '') {
        this.updateKey()
        window.location.assign('#/data')
      } else {
        this.makeToast()
        window.location.assign('#')
      }
    },
    // post_label () {
    //   axios.post(this.backendUrl + '/pull_data', {'target': this.COMMON.keyword}).then(response => (this.label1 = response.data))
    // },
    add_label () {
      axios.get(this.backendUrl + '/api/add_label')
      axios.get(this.backendUrl + '/api/show_label').then(response => (this.label1 = response.data.label1))
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  margin-top: 80px;
}
.headline{
  margin: auto;
  text-align: center;
}
.fade-enter-active, .fade-leave-active{
  transition: opacity 1s;
  -webkit-transition: opacity 1s;
}
.fade-enter, .fade-leave-to{
  opacity: 0;

}
.pic {
  width:100%;
  height:auto;
}
.banner {
  background: url('../assets/banner.png') no-repeat right;
  height: 360px;
  background-size: 500px 100%;
  opacity: 1;
  margin-bottom: 15px;
}
@media (max-width: 992px ){
  .banner{
    /* background: url('../assets/banner.png') no-repeat center; */
    background-size: 300px 240px;
  }
}
@media (max-width: 768px ){
  @media (min-width: 576px){
    .banner{
    background: url('../assets/banner.png') no-repeat center;
    }
  }
}
.intro1{
  background: url('../assets/hero4.png');
  height: 300px;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
.intro2{
  background: url('../assets/hero1.png');
  height: 300px;
  opacity: 1;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
.intro3{
   background: url('../assets/hero3.png');
  height: 300px;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
.intro-end{
   background: url('../assets/heroend.png');
  height: 120px;
}
.endblock{
  background-color: rgb(200, 200, 200)
}

</style>
