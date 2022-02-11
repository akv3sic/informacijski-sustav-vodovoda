import httpClient from '@/common/httpClient'

// initial state
const state = () => ({
    isLoading: true,
    categories: [],
 })
 
 // getters
 const getters = {
    categories(state) {
        return state.categories;
    },
    isLoading(state) {
        return state.isLoading;
    },
 }
 
 // actions
 const actions = {
    fetchCategories( {commit}) {
        commit('REQUEST')
        const url = '/cjenovnik/'
        httpClient.get(url)
            .then((response) => {
                console.log('response: ' + JSON.stringify(response.data))
                commit('SET_CATEGORIES', response.data)
            })
            .catch(err => {
                console.log(err)
             })
    },
    changeCategories({commit, dispatch}, payload){
        return new Promise((resolve, reject) => {
            commit('REQUEST')
            console.log('Šalje se ' + JSON.stringify(payload))
            httpClient.post("/cjenovnik/", payload)
            .then(response => {
                console.log(response)
                // check response status
                if(response.status === 200 || response.status === 201) { // OK
                    // assign response data
                    const msg = response.statusText
                    console.log(msg)
                    // call mutation
                    //commit('UPDATE_SUCCESS')
                    // call action to fetch updated user details
                    dispatch('fetchCategories')
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
    SET_CATEGORIES (state, payload) {
        state.categories = payload
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