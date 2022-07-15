<template>
    <div class="nav">
        <top-nav></top-nav>
    </div>
    <div class="main">

        <div class="title">
            <div class="product-title">
                {{ product.name }}
            </div>
            <div class="category-seller">
                <div class="category">
                    /{{ product.category }}
                </div>
                <div class="seller">
                    Sold by {{ product.seller }}
                </div>
            </div>
        </div>
        <div class="product-body">
            <div class="img-body">
                <img src="../../assets/product.png" alt="what now?">
            </div>
            <div class="buy">
                <div class="description">
                    <p class="description-title">What is {{ product.name }}?</p>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis ipsum soluta
                        necessitatibus, fuga ducimus consequatur praesentium, dolores odit maxime nisi molestiae
                        officiis sint inventore, non blanditiis quos pariatur et ipsam!</p>
                        <p class="price-tag">{{product.price}}$</p>
                </div>
                <div class="buy-button">
                    <div class="container">
                        <button class="checkout">
                            Add to cart
                        </button>

                        <button class="count" @click="order.count++">
                            <span class="material-symbols-rounded" v-if="order.count == 0">
                                add_shopping_cart
                            </span>
                            <label v-else>{{ order.count }}</label>
                        </button>
                    </div>

                </div>
            </div>
        </div>
        <div class="review-container">
            <div class="sub-container">
                <label class="sub-container-title">Opinion of our members</label>
                <div class="reviews">

                    <div class="review-box" v-for="review in product.reviews" :key="review.index">
                        <div class="review-head">
                            <div class="review-name">
                                {{ review.name }}
                            </div>

                            <div class="review-rate">
                                <span class="material-symbols-rounded">
                                    star
                                </span>
                                {{ review.rate }}
                            </div>
                        </div>
                        <div class="review-body">
                            <p class="review-text">
                                {{ review.text }}
                            </p>
                        </div>
                    </div>

                </div>
            </div>

            <div class="sub-container">
                <label class="sub-container-title">What do you think?</label>
                <div class="input-box" id="explaination-input">

                    <label>Write your own review:</label>
                    <textarea>

                    </textarea>
                    <button class="submit-button">
                        Submit
                    </button>
                </div>
            </div>
        </div>

    </div>

</template>

<script>
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
            product: {
                id: useRoute().params.id,
                name: "icecream",
                price: 5.25,
                seller: "diate",
                category: "diary",
                reviews:
                    [{
                        name: "Jack",
                        rate: 4.5,
                        text: "Lorem Ipsum kdaw hwaduoioahdowa hdwi"
                    },
                    {
                        name: "Jack",
                        rate: 4.5,
                        text: "Lorem Ipsum kdaw hwaduoioahdowa hdwi"
                    },
                    {
                        name: "Jack",
                        rate: 4.5,
                        text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis ipsum soluta necessitatibus fuga ducimus consequatur praesentium, dolores odit maxime nisi molestia officiis sint inventore non blanditiis quos pariatur et ipsam!"
                    },
                    {
                        name: "Jack",
                        rate: 4.5,
                        text: "Lorem Ipsum kdaw hwaduoioahdowa hdwi"
                    },
                    {
                        name: "Jack",
                        rate: 4.5,
                        text: "Lorem Ipsum kdaw hwaduoioahdowa hdwi"
                    },
                    {
                        name: "Jack",
                        rate: 4.5,
                        text: "Lorem Ipsum kdaw hwaduoioahdowa hdwi"
                    },
                    ],




            },
            order: {
                count: 0,
                product_id: useRoute().params.id,

            }
        }
    }
}  
</script>
<style lang="scss" scoped>
@import url("../../assets/style/shared.scss");
.main {
    button:active{
        background-color: transparent;
        color: $secondary;
    }
    
    width: 100%;
    height: calc(100vh - 220px);

    padding: 60px;
    font-family: "Inter";

    .title {
        display: flex;
        flex-direction: column;

        align-items: left;
        height: 100px;

        .product-title {
            font-size: 40px;
            font-weight: 800;
        }

        .category-seller {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            height: 60px;
            color: $gray-text;
            font-weight: 600;
        }

    }

    .product-body {
        display: flex;
        flex-direction: row;
        align-content: center;

        .buy {
            .description-title {
                font-size: 18px;
                font-weight: 650;
            }

            padding-top: 80px;
            width: 100%;

            .description {
                width: 40vw;
                .price-tag{
                    text-align: end ;
                    font-size: 18px;
                    font-weight: 600;
                }
            }

            .buy-button {
                display: flex;
                flex-direction: column-reverse;
                padding-right: 80px;
                padding-bottom: 80px;

                .container {
                    align-self: flex-end;
                    display: flex;
                    justify-content: space-between;

                    width: 200px;
                    height: 50px;
                    background-color: $main;
                    border-radius: 500px;
                    box-shadow: 0px -2px 4px $shadow;

                    padding-left: 18px;
                    padding-right: 18px;

                    padding-top: 12px;
                    padding-bottom: 12px;

                    align-items: center;

                    .checkout {
                        width: 100%;
                        height: 60px;
                        font-weight: 600;
                        font-size: 18px;
                        color: black;
                        justify-content: left;
                    }


                    .count {
                        width: 40px;
                        height: 40px;
                        font-size: 18px;
                        span{
                            display: flex;
                            justify-content: center;
                            align-items: center;

                            font-size: 24px;
                        }
                        font-weight: 600;
                        color: $secondary;


                        border-radius: 500px;
                    }


                }

            }
        }

        img {
            height: 40vh;
        }


    }

    .review-container {
        display: flex;
        justify-content: space-between;
        flex-direction: row;
        height: 100%;

        .sub-container {
            width: 50%;
            height: 100%;
          

            .sub-container-title {
                font-size: 20px;
                font-weight: 700;
            }
        }

        .input-box {
            margin-top: 30px;
            margin-left: 50px;
            height: 300px;
            width: 90%;
            background-color: $main;
            border-radius: 20px;
            padding: 16px;
            display: flex;
            justify-content: baseline;
            flex-direction: column;
            box-shadow: 0px 4px 8px $shadow;

            label {
                color: $secondary;
                font-weight: 500;
                width: fit-content;
                word-wrap: break-word;
                white-space: nowrap;
            }

            textarea {
                margin-top: 12px;
                color: $gray-text;
                height: 100%;
                width: 100%;

                border: 0px;
                font-family: "Inter";
                font-size: 15px;
                font-weight: 500;
              
            }

            textarea:focus {
                outline: none;
            }

            .submit-button {
                align-self: flex-end;
                display: flex;
                align-items: center;
                justify-content: center;

                padding-left: 12px;
                padding-right: 12px;
                padding-top: 12px;
                padding-bottom: 12px;
                background-color: $secondary;
                width: 100px;
                height: 50px;
                font-family: "Inter";
                color: $main;
                font-weight: 600;
                border-radius: 200px;

                span {
                    font-weight: 700;
                    font-size: 28px;
                }

                box-shadow: 0px 4px 8px $shadow;
            }

        }
    }

    .reviews {
        height: 40%;
        width: 80%;




        .review-box {

            width: 100%;
            border-radius: 18px;
            margin-left: 50px;
            margin-right: 50px;
            margin-top: 10px;

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
                display: flex;
                flex-direction: row-reverse;
                font-size: 16px;
                font-weight: 500;
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
}
</style>