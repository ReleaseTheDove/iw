<template>
  <div>
    <h2>I'm the Title</h2>
    <p>I'm the content.</p>
    <p>I'm the content.{{message}}</p>
    <h3>{{$store.state.counter}}</h3>
    <button @click="addition">+</button>
    <button @click="subtraction">-</button>
    <router-link to="/home/daily">Daily</router-link>
    <keep-alive>
      <router-view></router-view>
    </keep-alive>
  </div>
</template>

<script>

import {
  INCREMENT
} from '@/store/mutations-types'

export default {
  name: 'Home',
  data () {
    return {
      'message': 'Home'
    }
  },
  methods: {
    addition () {
      // this.$store.commit(INCREMENT)
      this.$store
          .dispatch('aupdate', 'will to increment.')
          .then(res => {
            console.log(res)
          })
    },
    subtraction () {
      this.$store.commit('decrement')
    }
  },
  activated () {
    this.$router.push('/home/daily')
  },
  beforeRouteLeave (to, from, next) {
    this.path = this.$route.path
    next()
  }
}
</script>