<template>
    <div class="main-parrent">
        <div class="logo-parrent">
            <img class="logo" src="../../../assets/white-logo.png">

            <button class="back-button" @click="BackToHome">
                <span class="material-symbols-rounded">arrow_back</span>
                <label> Go back to Homepage</label>
            </button>

        </div>

        <div class="form-parrent">
            <div class="title-parrent">
                <div class="account-type">
                    <img src="../../../assets/customers-logo.svg">
                </div>
                <div class="line">

                </div>
                <div class="slogan">
                    At <span>Exchequer</span> we value our partners
                </div>
            </div>
            <div class="form-content">
                <div class="input" id="first-name-input">
                    <label>First Name:</label>
                    <input type="text" v-model="entry.firstName">
                </div>
                <div class="input" id="last-name-input">
                    <label>Last Name:</label>
                    <input type="text" v-model="entry.lastName">
                </div>
                <div class="input" id="email-address-input">
                    <label>Email Address:</label>
                    <input type="text" v-model="entry.emailAddress">
                </div>
                <div class="input" id="phone-number-input">
                    <label>Username:</label>
                    <input type="text" v-model="entry.username">
                </div>
                <div class="input" id="company-input">
                    <label>Password:</label>
                    <input type="text" v-model="entry.password">
                </div>
                <div class="input-box" id="explaination-input">
                    <label>Any thing else we should know:</label>
                    <textarea>

                    </textarea>
                    <button class="submit-button" @click="signup()">
                        <span class="material-symbols-rounded">done</span>
                    </button>
                </div>

            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
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
    methods: {
        BackToHome: function () {
            this.$router.push({
                path: '/'
            })
        },
        async signup() {
                
            console.log(this.entry)
            const signupRes = await axios.post("http://localhost:8000/auth/users/", {
                username: "jack",
                password: "jack123",
                email: "jackie@gmail.com",
                first_name: "jack",
                last_name: "jackline",
            })
            console.log(signupRes)

        }
    },
    data() {
        return {
            entry: {
                username: null,
                password: null,
                firstName: null,
                lastName: null,
                emailAddress: null,

            }
        }
    }
}
</script>

<style lang="scss" scoped>
.main-parrent {
    display: block;

    background: linear-gradient(180deg, rgba(120, 231, 255, 0.35) 0%, #41B4F8 73.44%);
    position: relative;

    .logo-parrent {
        display: flex;
        position: relative;
        width: 100%;
        height: 200px;

        .back-button {
            position: absolute;
            top: 70px;
            right: 70px;
            width: 280px;
            display: flex;
            flex-direction: row;
            align-items: center;

            span {
                color: $main;
                font-size: 30px;
                margin-right: 4px;

            }

            label {
                font-weight: 500;
                font-size: 22px;
                width: fit-content;
                color: $main;
                word-wrap: break-word;
                white-space: nowrap;
            }
        }

        .logo {
            position: absolute;
            top: 70px;
            left: 70px;
            width: 260px;
        }

    }

    .form-parrent {
        position: relative;

        display: flex;
        justify-content: center;
        flex-direction: column;
        align-items: center;
        width: 55%;
        height: 64vh;
        margin-left: 200px;
        margin-top: 100px;
        padding: 70px;

        .title-parrent {
            left: 0px;
            display: flex;
            width: 100%;
            height: 12vh;

            .line {
                margin-left: 20px;
                margin-right: 20px;
                border: 4px solid $main;
                width: 0px;
            }

            .account-type {
                img {
                    height: 12vh;
                    margin-right: 20px;
                }
            }

            .slogan {

                width: 12vw;
                height: 12vh;
                font-family: "Inter";
                font-size: 26px;
                color: $main;

                span {
                    font-weight: 700;
                }
            }
        }

        .form-content {
            margin-top: 30px;
            left: 0px;
            display: grid;
            column-gap: 35px;
            row-gap: 25px;
            height: 100%;
            width: 100%;
            grid-template-columns: 1fr 1fr;
            grid-template-rows: repeat(8, 1fr);

            .input {

                filter: drop-shadow(0px 2px 18px rgba(0, 0, 0, 0.05));
                display: flex;
                flex-direction: row;

                align-items: center;
                height: 50px;
                background-color: $main;
                border-radius: 500px;
                padding: 16px;

                input {
                    width: 100%;
                    margin-left: 16px;
                    font-family: "Inter";
                    font-size: 15px;
                    font-weight: 400;
                    color: $gray-text;
                }

                label {
                    color: $secondary;
                    font-weight: 500;
                    width: fit-content;
                    word-wrap: break-word;
                    white-space: nowrap;

                }
            }

            #first-name-input {
                grid-row: 1;
                grid-column: 1;

            }

            #last-name-input {
                grid-row: 1;
                grid-column: 2;

            }

            #email-address-input {
                grid-row: 2;
                grid-column-start: 1;
                grid-column-end: 3;
            }

            #phone-number-input {
                grid-row: 3;
                grid-column: 1;

            }

            #company-input {
                grid-row: 3;
                grid-column: 2;
            }

            .input-box {
                grid-row-start: 4;
                grid-row-end: 9;
                grid-column-start: 1;
                grid-column-end: 3;
                background-color: $main;
                border-radius: 20px;
                padding: 16px;
                display: flex;
                justify-content: baseline;
                flex-direction: column;
                filter: drop-shadow(0px 2px 18px rgba(0, 0, 0, 0.05));

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
                    width: 50px;
                    height: 50px;
                    font-family: "Inter";
                    color: $main;
                    font-weight: 600;
                    border-radius: 200px;

                    span {
                        font-weight: 700;
                        font-size: 28px;
                    }

                    filter: drop-shadow(0px 2px 18px rgba(0, 0, 0, 0.05));
                }

            }

        }
    }
}
</style>