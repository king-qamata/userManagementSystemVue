import axios from 'axios'

export function requests(config) {
  const instance = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    timeout: 5000
  })

  return instance(config)
}
