import httpClient from '@/common/httpClient'

// initial state
const state = () => ({
    drawer: null,
    isLoading: true,
    contracts: [],
    selectedContract: 1
 })
 
 // getters
 const getters = {
    drawer(state) {
        return state.drawer
    },
    contracts(state) {
        return state.contracts;
    },
    isLoading(state) {
        return state.isLoading;
    },
    selectedContract(state) {
        return state.selectedContract;
    }
 }
 
 // actions
 const actions = {
    setDrawer( {commit}, payload) {
        commit('SET_DRAWER', payload)
    },
    setSelectedContract( {commit}, payload) {
        commit('SET_SELECTED_CONTRACT', payload)
    },
    fetchContracts( {commit}) {
        commit('REQUEST')
        const url = '/mojiprikljucci/'
        httpClient.get(url)
            .then((response) => {
                console.log('response: ' + JSON.stringify(response.data))
                commit('SET_CONTRACTS', response.data)
                commit('SET_SELECTED_CONTRACT', response.data[0].id)
            })
            .catch(err => {
                console.log(err)
             })
    },
 }
 
 // mutations
 const mutations = {
    SET_DRAWER (state, payload) {
        state.drawer = payload
    },
    SET_SELECTED_CONTRACT (state, payload) {
        state.selectedContract = payload
    },
    SET_CONTRACTS (state, payload) {
        state.contracts = payload
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