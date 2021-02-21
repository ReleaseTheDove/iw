import {
  INCREMENT
} from '@/store/mutations-types'

export default {
  aupdate (context, payload) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        context.commit(INCREMENT)
        console.log(payload)
        resolve('increment success')
      }, 1000);
    })
    
  }
}