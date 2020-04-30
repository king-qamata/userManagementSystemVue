import Vue from 'vue'
import Vuex from 'vuex'
// import mutations from './mutations'
// import actions from './actions'
// import getters from './getters'
import snackbar from './modules/Snackbar'
import users from './modules/Users'
import auth from './modules/Auth'
// import dataImport from './modules/DataImport'
// import tables from './modules/Tables'
import notificationsEmails from './modules/NotificationsEmails'
import dataStorage from './modules/DataStorage'
import systemEmail from './modules/SystemEmail'

Vue.use(Vuex)

//const state = {
  //count: 10
//}

// const store = new Vuex.Store({
export default new Vuex.Store({
  // state,
  // mutations,
  // actions,
  // getters,
  modules: {
    snackbar,
    users,
    auth,
    // dataImport,
    // tables,
    notificationsEmails,
    dataStorage,
    systemEmail
  },
  state: {},
  mutations: {},
  actions: {}
})
