import httpClient from '@/common/httpClient'

// initial state
const state = () => ({
    isLoading: true,
    malfunctionReports: [],
    activeTab: null
 })
 
 // getters
 const getters = {
    malfunctionReports(state) {
        return state.malfunctionReports;
    },
    isLoading(state) {
        return state.isLoading;
    },
    activeTab(state) {
        return state.activeTab
    },
 }
 
 // actions
 const actions = {
    fetchMalfunctionReports( {commit}, id) {
        // id = 1 --> aktivni
        // id = 2 --> završeni
        id == 0 ? id = null : id = id
        commit('REQUEST')
        const url = '/kvar/'
        //console.log("poslani param za izvješće: " + id)
        httpClient.get(url, {
            params: {
              id: id
            }
          })
            .then((response) => {
                //console.log('response: ' + JSON.stringify(response.data))
                commit('SET_MALFUNCTION_REPORTS', response.data)
            })
            .catch(err => {
                console.log(err)
             })
    },
    changeReportStatus({commit}, id){
        return new Promise((resolve, reject) => {
            commit('REQUEST')
            //console.log('Šalje se id kvara:' + id)
            httpClient.put("/kvar/", { id: id })
            .then(response => {
                //console.log(response)
                // check response status
                if(response.status === 200 || response.status === 201) { // OK
                    // assign response data
                    const msg = response.statusText
                    console.log(msg)
                    // call mutation
                    commit('REQUEST_SUCCESS')
                    resolve(response)
                }
            })
            .catch(err => {
                console.log(err)
                reject(err)
            })
        })
    },
    setActiveTab( {commit}, payload) {
        commit('SET_ACTIVE_TAB', payload)
    },
 }
 
 // mutations
 const mutations = {
    SET_MALFUNCTION_REPORTS (state, payload) {
        state.malfunctionReports = payload
        state.isLoading = false
    },
    SET_ACTIVE_TAB (state, payload) {
        state.activeTab = payload
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
