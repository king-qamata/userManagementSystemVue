import {
  login,
  register,
  recoveryAccount,
  resetPassword
} from '@/api/Auth.api'
import { Login } from '@/network/api'
import { Register } from '@/network/api'

export default {
  namespaced: true,
  state: {
    user: [],
    isLogged: false
  },
  getters: {
    getUser(state) {
      return state.user
    },
    getMe(state) {
      return state.user
    }
  },
  actions: {
    login({
      commit
    }, payload) {
      return login(payload)
    },
    signin({ commit
    }, payload) {
      return Login(payload)
    },
    register({
      commit
    }, payload) {
      return register(payload)
    },
    signup({
      commit
    }, payload) {
      return Register(payload)
    },
    recoveryAccount({ commit }, payload) {
      return recoveryAccount(payload)
    },
    resetPassword({ commit }, payload) {
      return resetPassword(payload)
    }
  },
  mutations: {
    SET_USER(state, data) {
      state.user = data
    },
    SET_LOGGED(state, value) {
      state.isLogged = value
    },
    SET_USER(state, payload) {
      state.user = payload
    }
  }
}
