import httpClient from '@/common/httpClient'

// initial state
const state = () => ({
    isLoading: true,
    places: [],
    streets: []
 })
 
 // getters
 const getters = {
    places(state) {
        return state.places;
    },
    streets(state) {
        return state.streets;
    },
    isLoading(state) {
        return state.isLoading;
    },
 }
 
 // actions
 const actions = {
    fetchPlaces( {commit}) {
        commit('REQUEST')
        const url = '/getmjesta/'
        httpClient.get(url)
            .then((response) => {
                console.log('response: ' + JSON.stringify(response.data))
                commit('SET_PLACES', response.data)
            })
            .catch(err => {
                console.log(err)
             })
    },
    fetchStreets( {commit}, place) {
        commit('REQUEST')
        const url = '/getulice/'
        httpClient.get(url, {
            params: { mjesto: place }
        })
            .then((response) => {
                console.log('response: ' + JSON.stringify(response.data))
                commit('SET_STREETS', response.data)
            })
            .catch(err => {
                console.log(err)
             })
    },

 }
 
 // mutations
 const mutations = {
    SET_PLACES (state, payload) {
        state.places = payload
        state.isLoading = false
    },
    SET_STREETS (state, payload) {
        state.streets = payload
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
