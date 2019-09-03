import { requests } from './request'

export const Login = params => {
  console.log(params)
  return requests({
    url: '/Login',
    data: params,
    method: 'post',
    headers: ({ 'Content-Type': 'application/x-www-form-urlencoded' })
  })
}

export const getList = () => {
  return requests({
    url: '/getList'
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

