#!/usr/bin/node
const process = require('process');
const axios = require('axios').default;
const fs = require('fs');

const URL = process.argv[2];
const filePath = process.argv[3];

axios.get(URL, {
}).then(response => {
  fs.writeFile(filePath, response.data, 'utf-8', err => {
    if (err) {
      console.log(err.message);
    }
  });
}).catch(err => {
  if (err) {
    console.log(err.message);
  }
});
