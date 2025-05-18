import axios from 'axios';
  // TODO rename commit (Upper_Case)

const state = {
  auth: {
    loggedIn: !!localStorage.getItem('accessToken'),
    accessToken: localStorage.getItem('accessToken') || null,
    refreshToken: localStorage.getItem('refreshToken') || null,
  },
  userDetails: JSON.parse(localStorage.getItem('userDetails')) || {},
};

const getters = {
  authAccessToken: (state) => state.auth.accessToken,
  authRefreshToken: (state) => state.auth.refreshToken,
  isLoggedIn: (state) => state.auth.loggedIn,
  userDetails: (state) => state.userDetails,
};

const actions = {
  async login({ commit }, { name, password }) {
    try {
      const response = await axios.post('/login', { name, password }, {
        headers: { 'No-Authorization': true },
      });

      const { access_token, refresh_token, user_details } = response.data;

      localStorage.setItem('accessToken', access_token);
      localStorage.setItem('refreshToken', refresh_token);
      localStorage.setItem('userDetails', JSON.stringify(user_details));

      commit('SET_USER_DETAILS', user_details);
      commit('SET_AUTH', {
        loggedIn: true,
        accessToken: access_token,
        refreshToken: refresh_token,
      });

      return { success: true };
    } catch (error) {
      console.error('Login failed:', error);
      return {
        success: false,
        message: error.response?.data?.message || 'An error occurred during login.',
      };
    }
  },
  clearAuth({ commit }) {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
    localStorage.removeItem('userDetails');

    commit('authLogout');
  },

  // refreshTokens({ commit }, { accessToken, refreshToken }) {
  //   localStorage.setItem('accessToken', accessToken);
  //   localStorage.setItem('refreshToken', refreshToken);

  //   commit('authSetAccessToken', accessToken);
  //   commit('authSetRefreshToken', refreshToken);
  //   commit('SET_AUTH', { loggedIn: true });
  // },
};

const mutations = {
  SET_USER_DETAILS(state, userDetails) {
    state.userDetails = userDetails;
  },
  SET_AUTH(state, auth) {
    state.auth = { ...state.auth, ...auth };
  },
  authSetAccessToken(state, token) {
    state.auth.accessToken = token;
  },
  authSetRefreshToken(state, token) {
    state.auth.refreshToken = token;
  },
  authLogout(state) {
    state.auth = {
      loggedIn: false,
      accessToken: null,
      refreshToken: null,
    };
    state.userDetails = {};
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
