import httpClient from '@/common/httpClient'

// initial state
const state = () => ({
    isLoading: true,
    requests: [],
    showSuccessAlert: false,
 })
 
 // getters
 const getters = {
    requests(state) {
        return state.requests;
    },
    isLoading(state) {
        return state.isLoading;
    },
    showSuccessAlert(state) {
        return state.showSuccessAlert;
    },
 }
 
 // actions
 const actions = {
    fetchRequests( {commit}) {
        commit('REQUEST')
        const url = '/zahtjevi/'
        httpClient.get(url)
            .then((response) => {
                console.log('popis zahtjeva: ' + JSON.stringify(response.data))
                commit('SET_REQUESTS', response.data.zahtjevi)
            })
            .catch(err => {
                console.log(err)
             })
    },
 }
 
 // mutations
 const mutations = {
    SET_REQUESTS (state, payload) {
        state.requests = payload
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
