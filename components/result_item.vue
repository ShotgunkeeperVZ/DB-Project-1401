<template>
    <div class="result-main">
        <div class="picture-like-wrapper">
            <button>
                <span class="material-symbols-rounded">
                    star
                </span>
            </button>
            <img src="../assets/icecream.jpg">
        </div>
        <div class="text-content">

            <div class="product-name box">
                {{ name }}
                <div class="review">
                    <div class="review-rate">
                        {{ rate }}
                        <span class="material-symbols-rounded">
                            star
                        </span>

                    </div>
                </div>
            </div>
            <div class="add-button box">
                <button class="add-to-basket">
                    Add
                    <span class="material-symbols-rounded">
                        add
                    </span>
                </button>
            </div>

            <div class="store-name box">
                {{ store }}
            </div>
            <div class="price box">
                {{ price }}$
            </div>
        </div>
    </div>

</template>
<script>
export default {
    props: {
        name: String,
        store: String,
        rate: Number,
        price: Number
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
            

        }
    },

    methods: {

    }
}
</script>
<style lang="scss" scoped>
.result-main {
    margin: 12px;
    font-family: "Inter";

    height: 320px;
    width: 220px;
    border-radius: 18px;
    box-shadow: 0px -2px 8px $shadow;

    .text-content {
        height: 120px;
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-template-rows: 1fr 1fr;
    }



    .add-button {

        grid-column: 2;
        grid-row: 1;
        justify-content: flex-end;

        .add-to-basket {
            width: 70px;
            height: 25px;
            border-radius: 20px;
            background-color: $secondary;
            box-shadow: 0px -2px 4px $shadow;
            display: flex;
            color: $main;
            padding-left: 8px;
            padding-right: 8px;
            padding-top: 4px;
            padding-bottom: 4px;
    
            font-size: 14px;
            font-weight: 600;

            justify-content: space-between;
            align-items: center;



        }

    }

    .store-name {
        grid-column: 1;
        grid-row: 2;
        font-weight: 600;
        font-size: 14px;
        color: $gray-text;
        align-items: flex-end;
        padding-bottom: 4px;


    }

    .product-name {
        grid-column: 1;
        grid-row: 1;
        font-weight: 700;
        font-size: 20px;
        display: flex;
        flex-direction: column;

        .review-rate {
            display: flex;

            align-items: center;
        }

        .review {
            span {
                font-size: 18px;
                color: $secondary;
            }

            font-size: 14px;
        }
    }

    .price {
        grid-column: 2;
        grid-row: 2;

        font-weight: 700;
        font-size: 18px;
        display: flex;
        flex-direction: row;
        justify-content: flex-end;
        align-items: flex-end;

    }

    .box {
        display: flex;
        width: 100%;
        height: 100%;
    }





    .picture-like-wrapper {
        position: relative;
        width: 220px;
        height: 200px;
        height: fit-content;

        img {
            border-radius: 18px 18px 0px 0px;
            object-fit: cover;
            width: 220px;
            height: 200px;
        }

        button {
            z-index: 5;
            position: absolute;
            height: 30px;
            width: 30px;
            top: 12px;
            right: 12px;
            display: flex;
            justify-content: center;
            align-items: center;
            border-radius: 500px;

            background-color: $main;
            box-shadow: 0px -2px 4px $shadow;

            span {
                z-index: 5;
                color: $secondary;
            }


        }
    }

    .text-content {
        padding: 12px;

    }

}
</style>