const { createProxyMiddleware } = require('http-proxy-middleware');

const backendAppProxyHost = process.env.BACKEND_APP_PROXY_HOST || 'localhost';

module.exports = function(app) {
  app.use(
    '/api',
    createProxyMiddleware({
      target:`http://${backendAppProxyHost}:8000`,
      changeOrigin: true,
    })
  );
};