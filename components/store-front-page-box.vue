<template>
    <div class="store-icon-front-page-parrent">
        <img src="../assets/store-logo.png">
        <div class="store-info">
            <label class="store-name">{{ storeName }}</label>
            <label class="store-address">{{ storeAddress }}</label>

            <label class="store-rating">
                <span class="material-symbols-rounded">
                    star
                </span>{{ storeRating }}</label>


        </div>
    </div>
</template>
<script>
export default {
    props: {
        storeName: String,
        storeRating: Number,
        storeAddress: String
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

.store-icon-front-page-parrent {
    font-family: "Inter";
    margin-left: 30px;
    width: 200px;
    height: auto;
    padding: 18px;
    border-radius: 18px;
    box-shadow: 0px 2px 8px $shadow;
    background-color: $main;

   

    img {
        width: 100%;
        border-radius: 18px;
        height: 60%;
    }

    .store-info {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: baseline;
        padding-top: 4px;
        padding-bottom: 8px;
        font-family: "Inter";
        font-size: 14px;
        min-height: 80px;

        .store-name {
            font-size: 18px;
            font-weight: 600;
            font-family: "Inter";
        }

        .store-address {
            font-size: 14px;
            font-weight: 500;
            font-family: "Inter";
        }   

        .store-rating {
            align-self: flex-end;
            font-size: 12px;
            font-weight: 500;
            display: flex;
            align-items: center;
            justify-content: space-evenly;
            justify-self: flex-end;
            font-family: "Inter";
            

            span {
                display: flex;
                justify-content: center;
                align-items: center;
                color: $secondary;
                font-size: 16px;
            }
        }
    }



}
</style>