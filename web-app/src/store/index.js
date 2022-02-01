import Vue from 'vue'
import Vuex from 'vuex'
import admin from './modules/admin'
import userDashboard from './modules/userDashboard'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    admin, userDashboard
  }
})
