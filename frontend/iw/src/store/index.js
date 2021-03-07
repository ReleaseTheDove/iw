import Vue from 'vue'
import Vuex from 'vuex'

import mutations from '@/store/mutations'
import actions from '@/store/actions'
import getters from '@/store/getters'
import moduleA from '@/store/modules/moduleA'

Vue.use(Vuex)

const state = {
  counter: 3,
  kline: {}
}

export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters,
  modules: {
    moduleA
  }
})
