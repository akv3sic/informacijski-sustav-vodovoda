import httpClient from '@/common/httpClient'

// initial state
const state = () => ({
    isLoading: true,
    consuption: [],
    graph: null 
 })
 
 // getters
 const getters = {
    consuption(state) {
        return state.consuption;
    },
    graph(state) {
        return state.graph;
    },
    isLoading(state) {
        return state.isLoading;
    },
 }
 
 // actions
 const actions = {

    fetchConsuption( {commit}, contractID) {
        commit('REQUEST')
        const url = '/potrosnja/'
        console.log('poslani prikljucak: ' + contractID)
        httpClient.get(url, {
            params: {
              idPrikljucka: contractID
            }
          })
            .then((response) => {
                console.log('response: ' + JSON.stringify(response.data))
                commit('SET_CONSUPTION', response.data.potrosnja)
                commit('SET_GRAPH', response.data.graf)
            })
            .catch(err => {
                console.log(err)
             })
    },
 }
 
 // mutations
 const mutations = {
    SET_CONSUPTION (state, payload) {
        state.consuption = payload
    },
    SET_GRAPH (state, payload) {
        state.graph = payload
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
