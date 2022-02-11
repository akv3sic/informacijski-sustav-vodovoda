import httpClient from '@/common/httpClient'
import Swal from 'sweetalert2'
// initial state
const state = () => ({
    isLoading: false,
 })
 
 // getters
 const getters = {
    isLoading(state) {
        return state.isLoading;
    }
 }
 
 // actions
 const actions = {
    postMalfunctionReport ({commit}, payload){
        return new Promise((resolve, reject) => {
            commit('REQUEST')
            console.log('Šalje se ' + JSON.stringify(payload))
            httpClient.post("/prijavakvara/", payload)
            .then(response => {
                console.log(response)
                // check response status
                if(response.status === 200 || response.status === 201) { // OK
                    // assign response data
                    const msg = response.statusText
                    console.log(msg)
                    // call mutation
                    commit('POST_REPORT_SUCCESS')
                    // call action to fetch updated payload details
                    resolve(response)
                }
            })
            .catch(err => {
                console.log(err)
                reject(err)
            })
        })
    }
 }
 
 // mutations
 const mutations = {
    SET_payload_DETAILS (state, payload) {
        state.payload = payload
    },
    REQUEST(state) {
        state.isLoading = true
    },
    POST_REPORT_SUCCESS(state) {
        state.isLoading = false
        /*********************************/
        /* successful registration alert */
        Swal.fire({
            width: 400,
            position: 'top-end',
            icon: 'info',
            title: 'Hvala. Vaša prijava je zaprimljena.',
            showConfirmButton: false,
            timer: 2500
        })
        /*********************************/
    }
 }
 
 export default {
     namespaced: true,
     state,
     getters,
     actions,
     mutations
 }