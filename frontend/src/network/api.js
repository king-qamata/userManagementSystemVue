import { requests } from './request'

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

