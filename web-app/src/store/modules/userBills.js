import httpClient from '@/common/httpClient'

// initial state
const state = () => ({
    isLoading: true,
    bills: [],
 })
 
 // getters
 const getters = {
    bills(state) {
        return state.bills;
    },
    isLoading(state) {
        return state.isLoading;
    },
 }
 
 // actions
 const actions = {

    fetchBills( {commit}, contractID) {
        commit('REQUEST')
        const url = '/mojiracuni/'
        console.log('poslani prikljucak: ' + contractID)
        httpClient.get(url, {
            params: {
              idPrikljucka: contractID
            }
          })
            .then((response) => {
                console.log('response: ' + JSON.stringify(response.data))
                commit('SET_BILLS', response.data.racuni)
            })
            .catch(err => {
                console.log(err)
             })
    },
 }
 
 // mutations
 const mutations = {
    SET_BILLS (state, payload) {
        state.bills = payload
        state.isLoading = false
    },
    REQUEST (state){
        state.isLoading = true
    },
 }
 
 export default {
     namespaced: true,
     state,
     getters,
     actions,
     mutations
 }