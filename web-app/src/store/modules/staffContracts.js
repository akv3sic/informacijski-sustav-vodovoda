import httpClient from '@/common/httpClient'

// initial state
const state = () => ({
    isLoading: true,
    contracts: [],
 })
 
 // getters
 const getters = {
    contracts(state) {
        return state.contracts;
    },
    isLoading(state) {
        return state.isLoading;
    },
 }
 
 // actions
 const actions = {
    fetchContracts( {commit}, {place, street}) {
        commit('REQUEST')
        let queryParams = null
        if(place) {
           queryParams = { mjesto: place }
        }
        if(street) {
            queryParams = { ulica: street }
         }
        const url = '/popisprikljucaka/'
        httpClient.get(url, { params: queryParams })
            .then((response) => {
                console.log('popis prikljucaka: ' + JSON.stringify(response.data))
                commit('SET_CONTRACTS', response.data.prikljucci)
            })
            .catch(err => {
                console.log(err)
             })
    },

 }
 
 // mutations
 const mutations = {
    SET_CONTRACTS (state, payload) {
        state.contracts = payload
        state.isLoading = false
    },
    REQUEST (state){
        state.isLoading = true
    },
    REQUEST_SUCCESS (state){
        state.isLoading = false
    },
 }
 
 export default {
     namespaced: true,
     state,
     getters,
     actions,
     mutations
 }
