import httpClient from '@/common/httpClient'
import Swal from 'sweetalert2'

// initial state
const state = () => ({
    isLoading: true,
    noOfBillsToBeActivated: [],
    showSuccessAlert: false,
 })
 
 // getters
 const getters = {
    noOfBillsToBeActivated(state) {
        return state.noOfBillsToBeActivated;
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
    fetchNoOfBillsToBeActivated( {commit}) {
        commit('REQUEST')
        const url = '/brojracuna/'
        httpClient.get(url)
            .then((response) => {
                console.log(JSON.stringify(response.data))
                commit('SET_NO_OF_BILLS_TO_BE_ACTIVATED', response.data.broj_racuna)
            })
            .catch(err => {
                console.log(err)
             })
    },
    activateAllBills({commit}) {
        return new Promise((resolve, reject) => {
            commit('REQUEST')
            httpClient.put("/upisbrojila/")
            .then(response => {
                console.log(response.data)
                // check response status
                if(response.status === 202) { //accepted
                    console.log(JSON.stringify(response.data))
                    // call mutation
                    commit('ACTIVATE_SUCCESS')
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
    SET_NO_OF_BILLS_TO_BE_ACTIVATED (state, payload) {
        state.noOfBillsToBeActivated = payload
        state.isLoading = false
    },
    REQUEST (state){
        state.isLoading = true
    },
    ACTIVATE_SUCCESS (state){
        state.isLoading = false
        /* succes alert */
        Swal.fire({
            width: 400,
            position: 'top-end',
            text: 'Računi uspješno aktivirani. Sad su vidljivi korisnicima.',
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
