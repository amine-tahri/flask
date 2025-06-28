import { createStore } from 'vuex'

import auth from './modules/auth'
import users from './modules/users'

const Store = createStore({
  modules: {
    auth,
    users,
  },
})
export default Store
