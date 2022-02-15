import httpClient from '@/common/httpClient'
import Swal from 'sweetalert2'

// initial state
const state = () => ({
    isLoading: true,
    requests: [],
    request: null,

 })
 
 // getters
 const getters = {
    requests(state) {
        return state.requests;
    },
    request(state) {
        return state.request;
    },
    isLoading(state) {
        return state.isLoading;
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
    fetchRequest( {commit}, requestID) {
        commit('REQUEST')
        const url = '/zahtjevi/' + requestID
        console.log('Request to' + url)
        httpClient.get(url)
            .then((response) => {
                console.log(response.data)
                commit('SET_REQUEST', response.data)
            })
            .catch(err => {
                console.log(err)
             })
    },
    approveRequest({commit}, id) {
        return new Promise((resolve, reject) => {
            commit('REQUEST')
            const url = '/zahtjevi/' + id + "/"
            httpClient.put(url)
            .then(response => {
                console.log(response.data)
                // check response status
                if(response.status === 202) { //accepted
                    console.log(JSON.stringify(response.data))
                    // call mutation
                    commit('APPROVE_SUCCESS')
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
    SET_REQUESTS (state, payload) {
        state.requests = payload
        state.isLoading = false
    },
    SET_REQUEST (state, payload) {
        state.request = payload
        state.isLoading = false
    },
    REQUEST (state){
        state.isLoading = true
    },
    APPROVE_SUCCESS (state){
        state.isLoading = false
        /* succes alert */
        Swal.fire({
            width: 400,
            position: 'top-end',
            text: 'Zahtjev odobren.',
            icon: 'success',
            showConfirmButton: false,
            timer: 2600
          })
    },
 }
 
 export default {
     namespaced: true,
     state,
     getters,
     actions,
     mutations
}