import axios from 'axios'

export function request (config) {
  const instance = axios.create({
    baseURL: process.env.API_ROOT,
    timeout: 10000
  })

  instance.interceptors.request.use(config =>{
    // console.log(config)
    return config
  }, err => {
    console.log(err)
  })

  instance.interceptors.response.use(res =>{
    // console.log(res)
    return res.data
  }, err => {
    console.log(err)
  })

  return instance(config)
}