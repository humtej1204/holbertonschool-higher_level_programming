#!/usr/bin/node
const axios = require('axios').default;
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

axios.get(url)
  .then(({ data }) => {
    /* console.log(data.characters); */
    data.characters.forEach((char) => {
      axios.get(char)
        .then(({ data }) => console.log(data.name))
        .catch(err => console.log(err.message));
    });
  })
  .catch(err => console.log(err.message));
