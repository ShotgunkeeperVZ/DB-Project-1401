export const state = () => ({
    token: null,
})

export const mutations = {
    setToken(state,value){
        state.token = value,
    }
}
export const getters = {
    getToken: state => state.token,
}