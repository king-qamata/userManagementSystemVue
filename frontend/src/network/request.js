import axios from 'axios'
import myConfig from './config'
export function requests(config) {
  const instance = axios.create({
    baseURL: myConfig.baseUrl,
    timeout: myConfig.timeout
  })

  return instance(config)
}
