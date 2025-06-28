import axios from 'axios';
import config from './config.json';

function setAuthorizationHeader(token) {
  if (token) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  } else {
    delete axios.defaults.headers.common['Authorization'];
  }
}

async function configure() {
  axios.defaults.baseURL = config.apiUrl;

  // 🔐 Request Interceptor
  axios.interceptors.request.use(
    async (request) => {
      const token = localStorage.getItem('accessToken');
      if (token && !request.headers['No-Authorization']) {
        request.headers['Authorization'] = `Bearer ${token}`;
      }
      return request;
    },
    (error) => Promise.reject(error)
  );

  // 🔁 Response Interceptor (Token Refresh Logic)
  axios.interceptors.response.use(
    (response) => response,
    async (error) => {
      const originalRequest = error.config;

      if (
        error.response &&
        error.response.status === 401 &&
        !originalRequest._retry &&
        !originalRequest.url.includes('/login') &&
        !originalRequest.url.includes('/refresh')
      ) {
        originalRequest._retry = true;

        const refreshToken = localStorage.getItem('refreshToken');
        if (!refreshToken) {
          window.location.href = '/login';
          return Promise.reject(error);
        }

        try {
          // 🔒 Use a fresh Axios instance to avoid interceptors
          const refreshAxios = axios.create({ baseURL: config.apiUrl });

          const response = await refreshAxios.post('/refresh', {}, {
            headers: {
              Authorization: `Bearer ${refreshToken}`,
            },
          });

          const { access_token } = response.data;
          localStorage.setItem('accessToken', access_token);

          // Attach new token to original request
          originalRequest.headers['Authorization'] = `Bearer ${access_token}`;

          return axios(originalRequest); // Retry original request
        } catch (refreshError) {
          localStorage.removeItem('accessToken');
          localStorage.removeItem('refreshToken');
          localStorage.removeItem('userDetails');
          window.location.href = '/login';
          return Promise.reject(refreshError);
        }
      }

      return Promise.reject(error);
    }
  );
}

export { configure, setAuthorizationHeader };
