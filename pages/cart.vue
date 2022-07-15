<template>
    <div class="main-parrent">
        <div class="nav">
            <top-nav></top-nav>
        </div>
        <label class="cart-label">Whats in your <span class="material-symbols-rounded">shopping_cart</span></label>
        <div class="main">

            <div class="side">
                <div class="cart-item-container scroll">
                    <div class="cart-item" v-for="item in cart" :key="item.index">
                        <img src="../assets/product.png">
                        <div class="text-container">
                            <div class="name-store">
                                <div class="name">
                                    {{ item.name }}
                                </div>
                                <div class="store">
                                    {{ item.store }}
                                </div>
                            </div>

                            <div class="price-count-close">
                                <button class="close" @click="removeFromCart(item.id)">
                                    <span class="material-symbols-rounded">close</span>
                                </button>
                                <div class="container">
                                    <label class="price-count">
                                        count: {{ item.count }} price of each: {{ item.price }}$
                                    </label>
                                    <label class="sum">
                                        Total price: {{ item.count * item.price }}$
                                    </label>
                                </div>

                            </div>
                        </div>

                    </div>


                </div>
                
            </div>


            <div class="side right-side">
                <label class="price-sum">Total: {{ totalPrice() }}$</label>
                
            </div>

        </div>
    </div>


</template>
<script>



export default {
    asyncData({ $pinia }) {
        this.store = useShopStore($pinia)
        console.log("ass")
    },
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
            cart: [

                {
                    name: "Ice cream",
                    store: "Hobby shop",
                    rate: 3.2,
                    price: 4.35,
                    count: 4,
                    stock: 54,
                    id: "kdlhsa98y1414314"
                },
                {
                    name: "Ice cream",
                    store: "Hobby shop",
                    rate: 3.2,
                    price: 4.35,
                    count: 4,
                    stock: 54,
                    id: "njklaSdh89y1234987"
                },
                {
                    name: "Ice cream",
                    store: "Hobby shop",
                    rate: 3.2,
                    price: 4.35,
                    count: 4,
                    stock: 54,
                    id: "klmd981828482714"
                },
                {
                    name: "Ice cream",
                    store: "Hobby shop",
                    rate: 3.2,
                    price: 4.35,
                    count: 4,
                    stock: 54,
                    id: "71649dhaw7d17623"
                },
                {
                    name: "Ice cream",
                    store: "Hobby shop",
                    rate: 3.2,
                    price: 4.35,
                    count: 4,
                    stock: 54,
                    id: "kdlhsa98y1414314"
                },
                {
                    name: "Ice cream",
                    store: "Hobby shop",
                    rate: 3.2,
                    price: 4.35,
                    count: 4,
                    stock: 54,
                    id: "njklaSdh89y1234987"
                },
                {
                    name: "Ice cream",
                    store: "Hobby shop",
                    rate: 3.2,
                    price: 4.35,
                    count: 4,
                    stock: 54,
                    id: "klmd981828482714"
                },
                {
                    name: "Ice cream",
                    store: "Hobby shop",
                    rate: 3.2,
                    price: 4.35,
                    count: 4,
                    stock: 54,
                    id: "71649dhaw7d17623"
                },
            ]



        }

    },
    methods: {
        removeFromCart: function (id) {
            for(let i = 0; i < this.cart.length; i++){
                if(this.cart[i].id === id){
                    this.cart.splice(i, 1);
                }
            }
        },
        totalPrice: function () {
            let sum = 0;
            for (let i = 0; i < this.cart.length; i++) {
                sum = sum + (this.cart[i].price * this.cart[i].count)
            }
            sum = sum.toFixed(2)
            return sum;
        }


    },
    computed: {


    },
    mounted() {


    }
}
</script>
<style lang="scss" scoped>
@import url("../assets/style/shared.scss");

.main {
    margin-bottom: 120px;

    width: 100%;
    padding: 60px;
    margin-bottom: 20px;
    font-family: "Inter";
    display: flex;
    flex-direction: row;

    

    .cart-item-container {
        width: 100%;
        display: flex;
        flex-direction: column;
        margin-bottom: 80px;
        height: calc(50vh);

        .cart-item {
            margin-bottom: 12px;
            width: 100%;
            display: flex;
            padding: 12px;


            img {
                border-radius: 18px 18px 0px 0px;
                object-fit: cover;
                width: 120px;
                height: 120px;
            }

            .text-container {
                width: 100%;
                height: 100%;
                display: flex;
                flex-direction: row;
                justify-content: space-between;
            }

            .name-store {
                align-self: center;

                .name {
                    font-weight: 700;
                    font-size: 20px;

                }

                .store {
                    font-weight: 600;
                    font-size: 14px;
                    color: $gray-text;
                }
            }

            .price-count-close {
                width: fit-content;
                height: 120px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;

                .close {
                    height: 35px;
                    width: 35px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    align-self: flex-end;

                }

                .close:active {
                    color: $gray-text;
                    border-radius: 500px;
                    background-color: transparent;


                }

                .container {

                    height: 100%;
                    display: flex;
                    flex-direction: column;
                    justify-content: flex-end;

                    .price-count {
                        font-size: 12px;
                        font-weight: 500;
                    }

                    .sum {
                        font-size: 16px;
                        font-weight: 500;
                    }
                }

            }
        }


    }

}

.price-sum {
    margin-left:100px;
    margin-top: 30px;
    font-family: "Inter";
    font-weight: 700;
    font-size: 24px;
}

.address-select {}

.delivery-method {}

.side {
    width: 50%;
}
.cart-label {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 20px;
        margin-left: 60px;
        margin-top: 60px;
        span {
            font-size: 40px;
        }

        color: $secondary;
    }
</style>