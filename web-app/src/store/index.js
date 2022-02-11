import Vue from 'vue'
import Vuex from 'vuex'
import admin from './modules/admin'
import userDashboard from './modules/userDashboard'
import auth from './modules/auth'
import userAccountDetails from './modules/userAccountDetails'
import userBills from './modules/userBills'
import userConsuptionOverview from './modules/userConsuptionOverview'
import adminConsuptionCategories from './modules/adminConsuptionCategories'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    admin, userDashboard, auth, userAccountDetails, userBills, userConsuptionOverview, adminConsuptionCategories
  }
})
