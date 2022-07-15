<template>
    <div class="main-parrent">
        <div class="nav">
        <top-nav></top-nav>
    </div>
    <div class="title-wrapper">
        <lable class="top-title">Here's what we found </lable>
    </div>
    
    <div class="main scroll">
        
        <div class="empty-state">

        </div>
        <result-item v-for="item in results" :key="item.index" :name="item.name" :store="item.store" :rate="item.rate" :price="item.price"></result-item>
    </div>
    </div>
    

</template>
<script>
import TopNav from '~~/components/top-nav.vue'
export default {
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
            api_results: [{
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },
            {
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },
            {
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },

            {
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },{
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },
            {
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },
            {
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },

            {
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },{
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },
            {
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },
            {
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },

            {
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },{
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },
            {
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },
            {
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },

            {
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },{
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },
            {
                name: "Bread",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },
            {
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },

            {
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },

            ],
            results: null
        }
    },
    methods: {
        filterApply: function(){
            let res = []
            for(let candid = 0; candid < this.api_results.length; candid++){
                 console.log("condition")
                if(this.api_results[candid].name.toLowerCase() === this.$route.params.search){
                    console.log("found")
                    res.push(this.api_results[candid])
                }
            }
            this.results = res;
        }
    },
    mounted() {
        this.filterApply();
    },

}
</script>
<style lang="scss" scoped>
@import url("../../assets/style/shared.scss");
.top-title{
    margin-left: 60px;
    margin-top: 60px;
    font-family: "Inter";
    font-size: 36px;
    font-weight: 700;
    padding-bottom: 20px;
  }
.title-wrapper{
    height:80px;
    display: flex;
    flex-direction: column-reverse;
}
.main {
    
    width: 100%;
    height: 60%;
    
    padding: 40px 60px 60px 60px;
    margin-bottom: 20px;
    font-family: "Inter";
    display: flex;  
  flex-wrap: wrap;
  justify-content: flex-start;
  margin-bottom: 120px;
  

}

body{
   
}
</style>