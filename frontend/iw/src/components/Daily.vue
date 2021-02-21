<template>
  <div>
    <h2>daily</h2>
    <div>
      <label for="code">code</label>
      <input :value="code" @keyup.enter="onSubmit" @blur='onSubmit' id="code"/>
    </div>
    <ul>
      <li v-for="item in Daily" 
          :key="item.trade_date">
          {{item}}
      </li>
    </ul>
  </div>
</template>

<script>
import {request} from '@/network/request'

export default {
  name: 'daily',
  data () {
    return {
      'code': '',
      'Daily': []
    }
  },
  methods: {
    onSubmit (event) {
      if (typeof(event) != 'undefined' && event.target.value !== this.code) {
        this.code = event.target.value
        request({
          url: '/api/stock/daily/'+this.code
        }).then(res => {
          this.Daily = res
        }).catch(err => {
          return err
        })
      }
    }
  },
  activated () {
    this.onSubmit()
  }
}
</script>