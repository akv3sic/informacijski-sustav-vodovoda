import httpClient from '@/common/httpClient'

// initial state
const state = () => ({
    isLoading: true,
    contracts: [],
    showSuccessAlert: false,
    noOfNewRequests: 0
 })
 
 // getters
 const getters = {
    contracts(state) {
        return state.contracts;
    },
    isLoading(state) {
        return state.isLoading;
    },
    showSuccessAlert(state) {
        return state.showSuccessAlert;
    },
    noOfNewRequests(state) {
        return state.noOfNewRequests;
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
                commit('SET_NO_OF_NEW_REQUESTS', response.data.broj_zahtjeva)
            })
            .catch(err => {
                console.log(err)
             })
    },
    // upis novog stanja brojila
    postNewEntry({commit}, {idPrikljucka, stanjeBrojila}) {
        return new Promise((resolve, reject) => {
            commit('REQUEST')
            const payload = {
                idPrikljucka: idPrikljucka,
                stanjeBrojila: parseInt(stanjeBrojila)
            }
            httpClient.post("/upisbrojila/", payload)
            .then(response => {
                console.log(response.data)
                // check response status
                if(response.status === 201 || response.status == 202) { // success
                    console.log(JSON.stringify(response.data))
                    // call mutation
                    commit('REQUEST_SUCCESS')
                    commit('NEW_ENTRY_SUCCESS')
                    resolve(response)
                }
            })
            .catch(err => {
                console.log(err)
                reject(err)
            })
        })
    },

 }
 
 // mutations
 const mutations = {
    SET_CONTRACTS (state, payload) {
        state.contracts = payload
        state.isLoading = false
    },
    SET_NO_OF_NEW_REQUESTS (state, payload) {
        state.noOfNewRequests = payload
    },
    REQUEST (state){
        state.isLoading = true
    },
    REQUEST_SUCCESS (state){
        state.isLoading = false
    },
    NEW_ENTRY_SUCCESS (state){
        state.showSuccessAlert = true
        setTimeout(() => { state.showSuccessAlert = false }, 5000)
    },
 }
 
 export default {
     namespaced: true,
     state,
     getters,
     actions,
     mutations
 }
