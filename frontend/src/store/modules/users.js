import axios from 'axios'

const API_BASE_PATH = '/users'

const state = {
  users: {
    items: [],
  },
}

const getters = {
  users: (state) => state.users.items,
}

const actions = {
  async fetchUsers({ commit }, payload) {
    let params = {
    }

    const { data } = await axios.get(API_BASE_PATH, { params })


    commit('SET_USERS', data.items)
  },
}

const mutations = {
  SET_USERS(state, items) {
    state.users.items = items
  },
}

export default {
  state,
  getters,
  actions,
  mutations,
}
