import httpClient from '@/common/httpClient'

// initial state
const state = () => ({
    isLoading: false,
    contracts: [],
    uploadProgress: 0,
    successAlert: false
 })
 
 // getters
 const getters = {
    isLoading(state) {
        return state.isLoading;
    },
    selectedContract(state) {
        return state.selectedContract;
    },
    uploadProgress(state) {
        return state.uploadProgress;
    },
    successAlert(state) {
        return state.successAlert;
    }
 }
 
 // actions
 const actions = {
    sendRequest({commit}, payload){
        return new Promise((resolve, reject) => {
            commit('REQUEST')
            console.log('Šalje se zahtjev' + JSON.stringify(payload))
            httpClient.post( '/zahtjevi/',
                payload,
                {
                headers: {
                    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"
                },
                // progress
                onUploadProgress: function(event) {
                    const percentCompleted = Math.round((event.loaded * 100) / event.total);
                    console.log('onUploadProgress', percentCompleted);
                    commit('SET_UPLOAD_PROGRESS', percentCompleted-2)
                }
                }
            )
            .then(response => {
                console.log(JSON.stringify(response))
                // check response status
                if(response.status === 200 || response.status === 201) { // OK
                    // call mutation
                    commit('REQUEST_SUCCESS')
                    commit('SET_UPLOAD_PROGRESS', 100)
                    resolve(response)
                    commit('RESET_UPLOAD_PROGRESS')
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
    SET_UPLOAD_PROGRESS (state, payload) {
        state.uploadProgress = payload
    },
    RESET_UPLOAD_PROGRESS (state) {
        setTimeout(function(){ state.uploadProgress = 0 }, 500 )
    },
    SET_CONTRACTS (state, payload) {
        state.contracts = payload
        state.isLoading = false
    },
    REQUEST (state){
        state.isLoading = true
    },
    REQUEST_SUCCESS (state){
        state.isLoading = false
        state.successAlert = true
        setTimeout(function(){ state.successAlert = false }, 4500 )
    },
 }
 
 export default {
     namespaced: true,
     state,
     getters,
     actions,
     mutations
 }