#!/usr/bin/node
const axios = require('axios');
const args = process.argv.slice(process.argv.length - 1);

axios({
  method: 'GET',
  url: args[0]
}).then(res => {
  console.log('code: '.concat(res.status));
}).catch(err => console.log('code: '.concat(err.response.status)));
