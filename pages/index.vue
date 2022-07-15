<template>
    <div class="main-parrent">
    <div class="nav">
      <top-nav></top-nav>
    </div>
    
    <div class="stores" v-if="stores != null">
      <label class="Title-Label">
        Stores Near You
        
      </label>
      <div class="stores-box">

        <store-front-page-box1 v-for="store in stores" :key="store.index" v-bind:storeName="store.name"
          v-bind:storeRating="store.rating" v-bind:storeAddress="store.address">
        </store-front-page-box1>


      </div>


    </div>

  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue'
import topNav from '../components/top-nav.vue'
import StoreFrontPageBox1 from '../components/store-front-page-box.vue'

export default {
  components: { topNav, StoreFrontPageBox1 },
  head() {
    return {
      link: [
        {
          rel: "stylesheet", href: "https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
        },
      ]
    }
  },
  data() {
    return {
      stores: [{name: "hobbye",
      address: "LA avn53 uj",
      rating: 4.1},
      {name: "hobbye",
      address: "LA avn53 uj",
      rating: 4.1},
      {name: "hobbye",
      address: "LA avn53 uj",
      rating: 4.1},{name: "hobbye",
      address: "LA avn53 uj",
      rating: 4.1}]

    }
  },
  computed: {

  },

  methods: {

  },
}



</script>


<style  lang="scss">
@import url("../assets/style/shared.scss");

body {
  margin: 0px;
  height: 100vh;
  width: 100vw;
}

.main-parrent {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;

  margin: 0px;
  width: 100%;
  height: 100vh;


  //grid-template-rows: calc(200px + max(20px, 3vh)) 1fr 2fr;

  .nav {
    height: 100%;
    width: 100vw;
    display: flex;
    background-color: white;
    grid-row-start: 1;
    grid-row-end: 3;


  }

  .stores {
    display: flex;
    flex-direction: column;
    background-color: $secondary;
    width: 100%;
    height: 40%;
    padding-left: 40px;
    padding-right: 40px;
    padding-top: 30px;
    padding-bottom: 60px;
    box-shadow: 0px -2px 16px $shadow;


    .Title-Label {
      color: $main;
      font-weight: 700;
      font-size: 28px;
    }

    .stores-box {
      margin-top: 16px;
      margin-left: 20px;
      display: flex;
      justify-content: flex-start;
      align-items: center;
      
    }
  }

}
</style>

<style lang="scss" scoped>
.prodcut-page-parrent {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

.product-info {
  width: 50vw;

  padding: 40px;
  height: 100%;
  flex-direction: column;
  display: flex;
  justify-content: space-evenly;

  .Product-title {
    display: flex;
    justify-content: baseline;
    align-items: center;

    label {
      align-self: center;
    }

    margin-top: 20px;
    font-size: 32px;
    font-weight: 800;
  }

  .product-action {
    height: 100%;
    width: 100%;
    padding: 12px;

    display: flex;
    justify-content: space-around;
    flex-direction: row;

    .product-picture {
      width: 300px;
      height: 300px;
      margin: 20px;
    }

    .price-label {

      font-size: 20px;
      font-weight: 700;
    }

    button {
      background-color: $secondary;
      width: 200px;
      padding: 18px;
      border-radius: 500px;
      height: 60px;
      font-family: "Inter";
      font-weight: 600;
      color: white;
    }
  }
}

.reviews {
  width: 50vw;
  height: 100%;

  .review-box {
    border-radius: 18px;
    margin-left: 50px;
    margin-right: 50px;
    margin-top: 30px;
    box-shadow: 0px 4px 8px $shadow;
    font-family: 'Inter';

    padding: 14px;

    .review-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-direction: row;
    }

    .review-name {
      font-size: 16px;
      font-weight: 600;
      color: black;
    }

    .review-rate {
      font-size: 14px;
      font-weight: 400;
      color: black;

      span {
        display: flex;
        justify-content: center;
        align-items: center;
        color: $secondary;
        font-size: 16px;
      }
    }

    .review-text {
      font-size: 14px;
      font-weight: 400;
      color: gray;
    }
  }
}
</style>