// next.config.js
module.exports = {
    async redirects() {
      return [
        {
          source: '/home',
          destination: '/',
          permanent: true,   // This causes a 301 redirect from /home to /
        },
      ];
    },
  };
  