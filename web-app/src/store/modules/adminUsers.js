import httpClient from '@/common/httpClient'
import Swal from 'sweetalert2'

// initial state
const state = () => ({
    isLoading: true,
    users: [],
 })
 
 // getters
 const getters = {
    users(state) {
        return state.users;
    },
    isLoading(state) {
        return state.isLoading;
    },
 }
 
 // actions
 const actions = {
    fetchUsers( {commit}, rolaID) {
        commit('REQUEST')
        const url = '/lista/'
        //console.log("poslana rola: " + rolaID)
        httpClient.get(url, {
            params: {
              rola: rolaID
            }
          })
            .then((response) => {
                //console.log('response: ' + JSON.stringify(response.data))
                commit('SET_USERS', response.data)
            })
            .catch(err => {
                console.log(err)
             })
    },
    addNewStaff({commit}, user) {
        return new Promise((resolve, reject) => {
            commit('REQUEST')
            httpClient.post("/registracija/", user)
            .then(response => {
                console.log(response.data)
                // check response status
                if(response.status === 201) { // resource created 
                    console.log(JSON.stringify(response.data))
                    // call mutation
                    commit('REQUEST_SUCCESS')
                    commit('ADD_STAFF_SUCCESS')
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
    SET_USERS (state, payload) {
        state.users = payload
        state.isLoading = false
    },
    REQUEST (state){
        state.isLoading = true
    },
    REQUEST_SUCCESS (state){
        state.isLoading = false
    },
    ADD_STAFF_SUCCESS() {
        /* success alert */
        Swal.fire({
            width: 400,
            position: 'top-end',
            icon: 'success',
            title: 'Djelatnik uspješno dodan.',
            showConfirmButton: false,
            timer: 1600
        })
        /*********************************/
    },
 }
 
 export default {
     namespaced: true,
     state,
     getters,
     actions,
     mutations
 }
