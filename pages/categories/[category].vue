<template>
    <div class="main-parrent">
        <div class="nav">
            <top-nav></top-nav>
        </div>
        <div class="current-cat-contain">
            <label class="current-cat">Currently at {{ currentCat }}</label>
        </div>


        <div class="category-list">
            <div class="category-item" v-for="cat in category" :key="cat.index" >
                <button @click="push(cat)">
                    {{ cat }}
                </button>
            </div>
        </div>

        <div class="filter-sort">

            <div class="filter">
              
                <div class="action-container">
                    <label>
                        Price
                    </label>
                    <div class="action">
                        <div class="input left" id="first-name-input">
                            <label>From:</label>
                            <input type="text" v-model="filter.price.lower">
                        </div>
                        <div class="input right" id="first-name-input">
                            <label>To:</label>
                            <input type="text" v-model="filter.price.higher">
                        </div>
                    </div>
                </div>

                <div class="action-container">
                    <label>
                        Rating
                    </label>
                    <div class="action">
                        <div class="input left" id="first-name-input">
                            <label>From:</label>
                            <input type="text" v-model="filter.rating.lower">
                        </div>
                        <div class="input right" id="first-name-input">
                            <label>To:</label>
                            <input type="text" v-model="filter.rating.higher">
                        </div>
                    </div>
                </div>

                <button class="apply-button" @click="filterApply()">
                    Apply
                </button>



            </div>
        </div>
        <div class="main scroll">
            <result-item v-for="item in results" :key="item.index" :name="item.name" :store="item.store"
                :rate="item.rate" :price="item.price"></result-item>
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
            category: ["Food", "Drinks", "NotDrinks", "Food", "Drinks", "NotDrinks", "Food", "Drinks", "Not Drinks"],
            results: [],
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
            }, {
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
            }, {
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
            }, {
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
            }, {
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },
            {
                name: "Ice cream",
                store: "Hobby shop",
                rate: 4.2,
                price: 1.35
            },
            {
                name: "Ice cream",
                store: "Hobby shop",
                rate: 1.2,
                price: 1
            },

            {
                name: "Ice cream",
                store: "Hobby shop",
                rate: 3.2,
                price: 4.35
            },

            ],
            currentCat: null,

            filter:{
                price: {
                    lower: 0,
                    higher: null
                },
                rating: {
                    lower: 0,
                    higher: 5
                }
            }

        }
    },
    methods: {
        push: function (index) {

            this.$router.push({
                path: '/categories/' + index
            })
        },
        filterApply: function(){
            let res = []
            for(let candid = 0; candid < this.api_results.length; candid++){
                 console.log("condition")
                if(this.api_results[candid].price >= this.filter.price.lower 
                && this.api_results[candid].price <= this.filter.price.higher 
                && this.api_results[candid].rate >= this.filter.rating.lower 
                && this.api_results[candid].rate <= this.filter.rating.higher){
                   
                    
                    res.push(this.results[candid])
                }
            }
            this.results = res;
        }
    },
    mounted() {
        
        this.currentCat = this.$route.params.category;
        this.results = this.api_results;

    },
    created(){
        
    }
}
</script>
<style lang="scss" scoped>
.current-cat-contain {
    margin-top: 60px;

    .current-cat {
        height: 80px;
        margin-left: 80px;
        font-family: "Inter";
        font-size: 24px;
        font-weight: 700;
        color: $secondary;
    }
}

.category-list {
    height: 60px;
    width: 100%;
    display: flex;
    flex-wrap: wrap;

    padding: 0px 60px 20px 60px;

    .category-item {
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 20px;
        font-weight: 600;
        color: #000;
        padding: 20px;


    }

    .category-item.selected {
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 20px;
        font-weight: 700;
        color: $secondary;
        padding: 20px;

    }


    font-family: "Inter";

}


.main {
    margin-bottom: 120px;

    width: 100%;

    height: 50%;


    padding: 40px 60px 60px 60px;
    margin-bottom: 20px;
    font-family: "Inter";
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;


}


.filter-sort {
    width: 100%;
    height: 100px;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    font-family: "Inter";
    flex-direction: row;
    .apply-button{
        padding-top: 8px;
        padding-bottom: 8px;
        padding-left: 12px;
        padding-right: 12px;
        height: 35px;
        border-radius: 18px;
        box-shadow: 0px 1px 2px $shadow;
        font-size: 14px;
        font-weight: 600;

    }

    .sort {
        display: flex;
        align-items: center;
        justify-content: space-evenly;
        width: 50%;

    }

    .filter {
        display: flex;
        align-items: center;
        justify-content: space-evenly;
        width: 50%;
        .action-container{
            display: flex;
            justify-content: space-between;
            width: 260px;
            align-items: center;
            label{
                font-weight: 700;
            }
        }
        .action {
            width: 200px;
            display: flex;
            flex-direction: row;
        }
    }

    .left {
        border-radius: 500px 0px 0px 500px;

    }

    .right {
        border-radius: 0px 500px 500px 0px;
    }



    .input {

        box-shadow: 0px 1px 2px $shadow;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        height: 35px;
        background-color: $main;

        padding: 10px;
        width: 100px;



        input {
            width: 100%;
            margin-left: 10px;
            font-family: "Inter";
            font-size: 10px;
            font-weight: 300;
            color: $gray-text;

            align-items: center;
        }

        button {
            min-width: 25px;
            min-height: 25px;
            border-radius: 500px;
            box-shadow: 0px 1px 2px $shadow;
            background-color: $secondary;
            display: flex;
            justify-content: center;
            align-items: center;

            span {
                font-size: 24px !important;
                color: #FFF;
            }

        }

        label {
            color: $secondary;
            font-size: 10px;
            font-weight: 300;
            width: fit-content;
            word-wrap: break-word;
            white-space: nowrap;

        }
    }
}
</style>