<template>
    <div class="prodcut-page-parrent" v-if="productFocus">
      <div class="product-info">
        <label class="Product-title">{{ product.name }}</label>
        <div class="product-action">
          <img class="product-picture" src="./assets/icecream.jpg">
          <label class="price-label">Price: {{ product.price }}$</label>
          <button class="add-to-cart-button">Add to Cart</button>
        </div>

      </div>
      <div class="reviews">
        <div class="review-box" v-for="review in reviews" :key="review.index">
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
</template>

<script>
export default {
    data() {
        return {
            reviews: [{
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
            ]
                
    
        }
    },
    methods: {


    }
}
</script>

<style lang="scss" scoped>



.product-info{
    padding: 40px;
    .product-title{
        margin-top: 20px;
        font-size: 24px;
        font-weight: 800;
    }
}
.reviews{
    height: 40%;
    width: 100vw;
    .review-box{
        border-radius: 18px;
        margin-left:50px;
        margin-right: 50px;
        margin-top:30px;
        box-shadow: 0px 4px 8px $shadow;
        font-family: 'Inter';
     
        padding: 14px;

        .review-head{
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-direction: row;
        }
        .review-name{
            font-size: 16px;
            font-weight: 600;
            color: black;
        }
        .review-rate{
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

        .review-text{
            font-size: 14px;
            font-weight: 400;
            color: gray;
        }
    }
}
</style>