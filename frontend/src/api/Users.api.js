import httpClient from './HttpClient';

const END_POINT = 'http://127.0.0.1:8000/api/v1/users/?format=json';

const getAllUsers = () => httpClient.get(END_POINT);
// you can pass arguments to use as request parameters/data
const getUser = (user_id) => httpClient.get(END_POINT, { user_id });
// maybe more than one..
const createUser = (username, password) => httpClient.post(END_POINT, { username, password });

const update = payload => httpClient.patch(`${END_POINT}/${payload.id_user}`,payload);

export {
    getAllUsers,
    getUser,
    createUser,
    update
}