#!/usr/bin/node
const axios = require('axios').default;
const ID = process.argv[2];
const endPoint = `https://swapi-api.hbtn.io/api/films/${ID}`;

axios.get(endPoint)
  .then(res => console.log(res.data.title))
  .catch(err => console.log(err.message));
