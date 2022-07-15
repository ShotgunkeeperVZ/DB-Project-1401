<template>

    <div class="nav-parrent">
        <div class="status-bar">
            <label class="status-bar-label" id="location-status-bar-label">{{ location }}</label>
            <label class="status-bar-label" id="time-status-bar-label">{{ time }}</label>
            <label class="status-bar-label" id="order-status-bar-label">{{ order }}</label>
        </div>
        <div class="nav-body">
            <div class="logo-account">
                <div class="logo">
                    <img src="../assets/logo.svg">
                </div>
            </div>

            <div class="search">
                <div class="search-input">
                    <input type="text" v-model="searchQueary" class="search-input-entry" placeholder="Search">

                </div>
                <div class="search-button">
                    <button @click="search()" class="search-button-button">
                        <span class="material-symbols-rounded">
                            search
                        </span>
                    </button>
                </div>
            </div>
            <div class="account">

                <div id="account-name" @click="openAccountPanel()">
                    <span class="material-symbols-rounded" v-if="loggedIn">expand_more</span>
                    <label v-if="loggedIn">
                        {{ account.name }}
                    </label>
                    <div v-if="!loggedIn" class="log-in">
                        <div class="input" id="first-name-input" >
                            <label>Username:</label>
                            <input type="text" v-model="entry.username">
                        </div>
                        <div class="input" id="last-name-input">
                            <label>Password:</label>
                            <input type="text" v-model="entry.password">
                            <button class="log-in-buttton" @click="login()">
                                <span class="material-symbols-rounded">
                                    chevron_right</span>
                            </button>
                        </div>
                    </div>



                </div>
            </div>
            <div class="checkout">
                <button class="checkout-button">Cart</button>
                <button class="basket-button">
                    <span class="material-symbols-rounded">
                        shopping_cart
                        <div class="shopping-cart-count" v-if="shoppingCartCount != 0">
                            {{ shopingCartCount }}
                        </div>

                    </span>

                </button>
            </div>
        </div>
        <!-- <div class="results-account-info">
            <div class="result" v-if="searchFocus"></div>
           
            <div class="account-info" v-if="accountFocus">
                <div class="log-in-box" v-if="!loggedIn">
                    <label class="log-in-label">Sign-in</label>
                    <div class="form-couplers">
                        <input class="log-in-input" type="text" placeholder="Username">
                        <input class="log-in-input" type="text" placeholder="Password">
                    </div>
                    <div class="sign-button-wrapper">
                        <button class="Account-Button">Log-in</button>
                    </div>
                </div>

                <div class="sign-in-box" v-if="!loggedIn">
                    <label class="log-in-label">Sign-up</label>
                    <div class="form-couplers">
                        <input class="log-in-input" type="text" placeholder="First Name">
                        <input class="log-in-input" type="text" placeholder="Last Name">
                    </div>
                    <div class="form-couplers">
                        <input class="log-in-input" type="text" placeholder="Email Address">
                    </div>
                    <div class="form-couplers">
                        <input class="log-in-input" type="text" placeholder="Password">
                        <input class="log-in-input" type="text" placeholder="Conformation">
                    </div>
                    <div class="sign-button-wrapper">
                        <button class="Account-Button">Sign-up</button>
                    </div>
                    
                </div>
                <div class="account-info-box">

                </div>
            </div>
           
        </div>
         -->
    </div>


</template>

<script lang="ts">
import axios from "axios"
export default {
    data() {
        return {

            time: null,
            interval: null,
            location: this.currentLocation(),
            order: this.currentOrder(),
            searchQueary: null,
            loggedIn: false,
            shoppingCartCount: 0,
            accountFocus: false,
            account: {
                name: "jessie",

            },

            entry: {
                username: null,
                password: null
            },
            token: null

        }
    },

    computed: {


    },
    /*beforeDestroy() {
        // prevent memory leak
        clearInterval(this.interval)
    },
    created() {
         
        this.interval = setInterval(() => {
            // Concise way to format time according to system locale.
            // In my case this returns "3:48:00 am"
            this.time = Intl.DateTimeFormat(navigator.language, {
                hour: 'numeric',
                minute: 'numeric',
                second: 'numeric'
            }).format()
        }, 1000)
    },*/
    methods: {

        currentLocation() {
            return "New York"
            /*TODO*/
        },
        currentOrder() {
            return "ETA: " + "15m"
            /*TODO*/
        },
        search() {
            alert();
        },
        openAccountPanel() {
            if (!this.loggedIn) {
                this.accountFocus = !this.accountFocus;
            }

        },
        async login (){
            const res = await axios.post("http://localhost:8000/auth/jwt/create",{
                username: this.entry.username,
                password: this.entry.password,
            });
            if(res.status){
                this.token = res.data.access;
                this.loggedIn = true;
                this.account.name = this.entry.username;
                this.$store.mutations.setToken(res.data.access);
            }
        }



    },
}
</script>

<style lang="scss" scoped>
@import url("../assets/style/shared.scss");

.log-in {
    display: flex;
    flex-direction: column;
    justify-content: space-evenly !important;
    align-items: center;
    height: 80px;
}

.input {

    box-shadow: 0px 1px 2px $shadow;
    display: flex;
    flex-direction: row;
    align-items: center;
    height: 35px;
    background-color: $main;
    border-radius: 500px;
    padding: 10px;
    min-width: 220px;

    input {
        width: 100%;
        margin-left: 10px;
        font-family: "Inter";
        font-size: 10px;
        font-weight: 300;
        color: $gray-text;

        align-items: center;
    }

    .log-in-buttton {
        
        min-width: 25px;
        min-height: 25px;
        border-radius: 500px;
        box-shadow: 0px 1px 2px $shadow;
        background-color: $secondary;
        display: flex;
        justify-content: center;
        align-items: center;
        span{
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

.results-account-info {
    background-color: transparent;
    height: 70%;
    grid-row-start: 2;
    grid-row-end: 3;
    width: 100%;
    display: flex;
    box-sizing: border-box;


    .account-info {
        padding: 18px;
        background-color: transparent;
        height: 100%;
        width: 100vw;
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        flex-direction: row;

        .log-in-label {
            color: $secondary;
            font-weight: 700;
            font-size: 22px;
            padding-left: 20px;
        }

        .form-couplers {
            display: flex;
            align-items: center;
            justify-content: space-evenly;
            margin-top: 12px;
        }

        .sign-button-wrapper {
            display: flex;
            align-items: flex-end;
            height: 100%;
            justify-content: right;

        }

        button {
            margin-left: 16px;
            margin-right: 16px;
            padding: 16px;
            background-color: $secondary;
            color: $main;
            font-weight: 600;
            border-radius: 500px;
            width: 100px;
            font-size: 16px;

            margin-top: 20px;
            font-family: "Inter";
            box-shadow: 0px 2px 8px $shadow;


        }

        button:active {
            box-shadow: inset 0px 2px 8px $shadow;
            background-color: $main;
            color: $secondary;
        }

        .log-in-box {
            display: flex;
            padding-top: 12px;
            padding-bottom: 12px;
            width: 100%;
            height: 100%;
            padding-left: 20px;
            padding-right: 20px;
            flex-direction: column;
            margin-right: 30px;


        }

        .sign-in-box {
            display: flex;
            width: 100%;
            height: 100%;
            display: flex;
            padding-top: 12px;
            padding-bottom: 12px;
            padding-left: 20px;
            padding-right: 20px;
            flex-direction: column;
            margin-left: 30px;
        }

        .log-in-input {
            margin-left: 16px;
            margin-right: 16px;
            margin-top: 16px;
            padding-top: 8px;
            padding-bottom: 8px;
            padding-left: 16px;
            padding-right: 16px;
            height: 40px;
            border-radius: 500px;
            box-shadow: inset 0px 2px 4px $shadow;
            font-size: 14px;
            font-weight: 600;
            font-family: "Inter";
            width: min(100%);

        }
    }

    .results {
        background-color: transparent;
        height: 100%;
        width: 100vw;
        display: flex;
    }

}


.status-bar {
    padding-top: 4px;
    padding-bottom: 4px;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    width: 100vw;
    margin: 0px;
    background-color: $secondary;
    height: max(20px, 3vh);
}

.status-bar-label {
    color: $main;
    font-weight: 600;
    font-size: 12px;
}

.nav-parrent {
    display: flex;
    flex-direction: column;
    width: 100vw;
    height: 250px;
}

.nav-body {

    height: 180px;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    padding-left: 60px;
    padding-right: 60px;
    box-shadow: 0px 2px 16px $shadow;


    .logo-account {
        margin-left: 0px;
        margin-right: 40px;
        display: flex;
        justify-content: space-evenly;
        align-items: center;
        height: 100%;
        flex-direction: column;
        width: max(275px, 15vw);

        .logo {
            padding: 4px;
            display: flex;
            justify-content: center;
            align-items: center;

            img {
                display: flex;
                justify-content: center;
                align-items: center;
            }
        }

        .account {
            display: grid;

            height: 60px;
            margin-top: 8px;

            .sign-in-button {
                .account-profile {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    margin-right: 18px;

                    span {
                        font-size: 40px;
                        font-weight: 500;
                        color: $secondary;
                    }

                }

                .arrow-icon {
                    display: flex;
                    justify-content: center;
                    align-items: center;

                    span {
                        font-size: 44px;
                        font-weight: 500;
                    }

                }

                button:active {
                    background-color: $secondary;
                    color: $main;
                    box-shadow: inset 0px 2px 4px $shadow;

                    span {
                        color: $main;
                        font-weight: 600;
                    }
                }

            }



        }
    }

    .search {
        margin-left: 40px;
        margin-right: 40px;
        display: grid;
        grid-template-columns: 1fr 60px;
        width: 100%;
        height: 60px;
        border-radius: 500px;
        background-color: $alt-main;
        box-shadow: inset 0px 2px 8px $shadow;

        .search-input {
            width: 100%;
            height: 100%;
            padding: 6px;

            .search-input-entry {
                font-family: "Inter";
                color: $gray-text;
                font-size: 16px;
                font-weight: 400;
                height: 100%;
                width: 100%;
                background: transparent;
                padding: 8px;
            }
        }

        .search-button {
            padding: 8px;

            .search-button-button {
                background-color: $secondary;
                border-radius: 500px;
                width: 100%;
                height: 100%;
                border: none;
                box-shadow: 0px 2px 8px $shadow;
                display: flex;
                justify-content: center;
                align-items: center;

                span {
                    color: $main;
                    font-size: 28px;
                    font-weight: 800;
                }

            }

            .search-button-button:active {
                background-color: $main;
                box-shadow: inset 0px 2px 8px $shadow;

                span {
                    color: $secondary;

                }
            }
        }


    }

    .checkout {
        margin-left: 40px;
        margin-right: 40px;
        display: grid;
        grid-template-columns: max(120px, 8vw) 60px;
        height: 60px;
        border-radius: 500px;
        width: max(150px, 10vw);

        box-shadow: 0px 2px 8px $shadow;

        .checkout-button {
            height: 60px;
            width: 100%;
            font-family: "Inter";
            font-weight: 600;
            color: $main;
            background-color: $secondary;
            padding: 4px;
            padding-left: 16px;
            padding-right: 16px;
            border-right: 4px solid #73CBFF;
            border-radius: 500px 0px 0px 500px;
        }

        .basket-button {
            height: 60px;
            width: 100%;
            color: $main;
            padding: 8px;
            background-color: $secondary;
            border-radius: 0px 500px 500px 0px;
            display: flex;
            justify-content: center;
            align-items: center;

            span {
                z-index: 1;
                color: $main;
                font-size: 28px;
                font-weight: 800;
                position: relative;

                .shopping-cart-count {
                    z-index: 2;
                    width: 22px;
                    height: 22px;
                    background-color: $super;
                    border-radius: 500px;
                    font-family: "Inter";
                    font-weight: 600;
                    font-size: 14px;
                    position: absolute;
                    right: -5px;
                    bottom: -5px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }
            }

        }


    }




}

/*#account-name {
    font-family: "Inter";
    color: $text;
    font-weight: 600;
    font-size: 18px;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    text-align: center;
    margin-left: 30px;
    margin-right: 30px;

    div {
        display: flex;
        justify-content: center;
        align-items: center;

        button {
            margin: 8px;
            padding: 12px;
            padding-left: 8px;
            padding-right: 8px;
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: center;
            width: 120%;
            height: 50px;
            font-size: 18px;
            font-weight: 700;

            span {
                margin-left: 8px;
                display: flex;
                justify-content: center;
                align-items: center;
                color: $secondary;
                font-size: 28px;
                font-weight: 700;
            }

            border-radius: 500px;
            box-shadow: 2px 2px 4px $shadow;
        }
    }
}*/
</style>