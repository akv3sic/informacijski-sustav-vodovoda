import httpClient from '@/common/httpClient'

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
 }
 
 export default {
     namespaced: true,
     state,
     getters,
     actions,
     mutations
 }
