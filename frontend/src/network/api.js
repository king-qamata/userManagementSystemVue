import { requests } from './request'

export const Login = payload => {
  console.log(payload)
  return requests({
    url: '/signin/',
    data: payload,
    method: 'post',
    headers: ({ 'Content-Type': 'application/x-www-form-urlencoded' })
  })
}

export const Register = params => {
  console.log(params)
  return requests({
    url: '/api/v1/users/signup/',
    data: params,
    method: 'post',
    headers: ({ 'Content-Type': 'application/x-www-form-urlencoded' })
  })
}

export const getList = () => {
  return requests({
    url: '/api/v1/users/?format=json',
    headers: ({ 'Content-Type': 'application/x-www-form-urlencoded' })
  })
}

export const addUser = params => {
  return requests({
    url: '/addUser',
    params
  })
}

export const removeUser = params => {
  return requests({
    url: '/removeUser',
    params
  })
}

export const editUser = params => {
  return requests({
    url: '/editUser',
    params
  })
}

export const uploadAD = (params) => {
  return requests({
    url: '/upload/' + new Date().getTime(),
    data: params,
    headers: ({ 'Content-Type': 'multipart/form-data' }),
    method: 'post'
  })
}

export const getADList = () => {
  return requests({
    url: '/getADList'
  })
}

