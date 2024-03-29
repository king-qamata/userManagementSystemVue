import httpClient from './HttpClient';

const END_POINT = 'http://127.0.0.1:8000/signin/';

const login = payload => httpClient.post(END_POINT, payload);

const register = payload => httpClient.post('auth/register',payload);

const recoveryAccount = payload => httpClient.post('/auth/recovery',payload);

const resetPassword = payload => httpClient.post('/auth/resetpassword',payload);

export {
    login,
    register,
    recoveryAccount,
    resetPassword
}