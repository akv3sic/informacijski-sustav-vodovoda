import Vue from 'vue'
import Vuex from 'vuex'
import admin from './modules/admin'
import userDashboard from './modules/userDashboard'
import auth from './modules/auth'
import userAccountDetails from './modules/userAccountDetails'
import userBills from './modules/userBills'
import userConsuptionOverview from './modules/userConsuptionOverview'
import userMalfunctionReport from './modules/userMalfunctionReport'
import adminConsuptionCategories from './modules/adminConsuptionCategories'
import adminUsers from './modules/adminUsers'
import adminMalfunctionReports from './modules/adminMalfunctionReports'
import placesAndStreets from './modules/placesAndStreets'
import staffContracts from './modules/staffContracts'
import userNewContractRequest from './modules/userNewContractRequest'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    admin, userDashboard, auth, userAccountDetails, userBills, userConsuptionOverview, adminConsuptionCategories,
    userMalfunctionReport, adminUsers, adminMalfunctionReports, placesAndStreets, staffContracts,
    userNewContractRequest
  }
})
