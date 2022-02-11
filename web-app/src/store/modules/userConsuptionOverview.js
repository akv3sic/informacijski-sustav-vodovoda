import httpClient from '@/common/httpClient'

// initial state
const state = () => ({
    isLoading: true,
    consuption: [],
 })
 
 // getters
 const getters = {
    consuption(state) {
        return state.consuption;
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
