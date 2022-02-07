import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";

Vue.use(VueAxios, axios)


const httpClient = Vue.axios.create({
    baseURL: process.env.VUE_APP_BASE_URL,
    headers: {
        "Content-Type": "application/json",
    }
});

if(window.localStorage.getItem('token')) { 
    let token = 'Token ' + window.localStorage.getItem('token')
    httpClient.defaults.headers.common['Authorization'] = token || ""
}

export default httpClient;