<template>
    <div class="main-parrent">
        <div class="nav">
            <top-nav></top-nav>
        </div>
        <div class="store-info">
            <div class="store-logo">
                <img src="../../assets/store-logo.png">
            </div>
            <div class="name-address">
                <p class="name">{{store.name}}</p>
                <p class="address">{{store.address}}</p>
            </div>
            <div class="rating">
                <div class="rating-wrapper">
                    {{store.rating}}
                <span class="material-symbols-rounded">
                            star
                        </span>
                </div>
                
            </div>
        </div>
        <div class="main scroll">

            <div class="empty-state">

            </div>
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
            results: [{
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
            store: {
                name: "Hoblin. Co.",
                rating: 4.5,
                address: "Nyc 45th w and 5th avenue"
            }
        }
    }

}
</script>
<style lang="scss" scoped>
@import url("../../assets/style/shared.scss");
.store-info {
    height: 200px;
    width: 100%;
    display: flex;
    flex-direction: row;
    margin-bottom: 40px;
    padding: 20px 240px 0px 60px;


    font-family: "Inter";
    .name-address{
        .name{
            font-size: 38px;
        font-weight: 700;
        padding-top: 20px;
        white-space: nowrap;
        }

        .name-address{
            width: fit-content;
            font-size: 22px;
        font-weight: 600;
        padding-top: 20px;
        color: $gray-text;
        white-space: nowrap;
        }
        


    }

    .rating{
        font-size: 28px;
        font-weight: 600;
        margin-top: 60px;
        display: flex;
        
        flex-direction: column;
        span{
            color: $secondary;
            font-size: 44px;
            margin-left: 4px;
        }
        width: 100%;
        .rating-wrapper{
            padding-left: 60px;
            display: flex;
            justify-content: flex-start;
            align-items: center;
        }
    }

    img {
        height: fit-content;
        border-radius: 18px 18px 0px 0px;
        object-fit: cover;
        width: 220px;
        height: 200px;
    }
}

.top-title {
    margin-left: 60px;
    margin-top: 60px;
    font-family: "Inter";
    font-size: 36px;
    font-weight: 700;
    padding-bottom: 20px;
}

.title-wrapper {
    height: 80px;
    display: flex;
    flex-direction: column-reverse;
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

body {
    
}
</style>