import {
  INCREMENT
} from '@/store/mutations-types'

export default {
  [INCREMENT] (state) {
    state.counter++
  },
  decrement (state) {
    state.counter--
  }
}