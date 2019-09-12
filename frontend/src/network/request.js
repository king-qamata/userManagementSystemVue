import axios from 'axios'
import myConfig from './config'
import Cookies from 'js-cookie'
import router from '@/router'
import qs from 'qs'

export function requests(config) {
  return new Promise((resolve, reject) => {
    const instance = axios.create({
      baseURL: myConfig.baseUrl,
      timeout: myConfig.timeout
    })
    // 拦截器
    instance.interceptors.request.use(
      config => {
        const token = Cookies.get('token')
        if (token) {
          // console.log(config.headers)
          config.headers.accessToken = token
          // console.log(config.headers)
        } else {
          router.push({ path: '/login' })
        }
        if (config.method === 'post') {
          if (config.url.indexOf('upload') === -1) {
            config.data = qs.stringify(config.data)
          }
        }
        return config
      },
      error => {
        if (error.code === 'ECONNABORTED' && error.message.indexOf('timeout') !== -1) {
          console.log('timeout请求超时')
        }
        return Promise.reject(error)
      })

    // response 拦截器
    instance.interceptors.response.use(
      response => {
        // let data
        // // IE9时response.data是undefined，因此需要使用response.request.responseText(Stringify后的字符串)
        // if (response.data === undefined) {
        //   data = JSON.parse(response.request.responseText)
        // } else {
        //   data = response.data
        // }
        // console.log(data)
        // 根据返回的code值来做不同的处理
        // switch (data.rc) {
        //   case 1:
        //     console.log(data.desc)
        //     break
        //   case 0:
        //     store.commit('changeState')
        //     // console.log('登录成功')
        //     break
        //   default:
        // }
        // return data
        return response
      },
      err => {
        if (err && err.response) {
          switch (err.response.status) {
            case 400:
              err.message = '请求错误'
              break
            case 401:
              err.message = '未授权，请登录'
              break
            case 402:
              err.message = '登录失败'
              break
            case 403:
              err.message = '拒绝访问'
              break
            case 404:
              err.message = `请求地址出错: ${err.response.config.url}`
              break
            case 408:
              err.message = '请求超时'
              break
            case 500:
              err.message = '服务器内部错误'
              break
            case 501:
              err.message = '服务未实现'
              break
            case 502:
              err.message = '网关错误'
              break
            case 503:
              err.message = '服务不可用'
              break
            case 504:
              err.message = '网关超时'
              break
            case 505:
              err.message = 'HTTP版本不受支持'
              break
            default:
          }
        }
        console.error(err)
        return Promise.reject(err) // 返回接口返回的错误信息
      }
    )

    instance(config)
      .then(res => {
        resolve(res)
        return false
      })
      .catch(err => reject(err))
  })
}
