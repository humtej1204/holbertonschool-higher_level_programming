#!/usr/bin/node
const axios = require('axios');
const apiUrl = process.argv[2];

axios.get(apiUrl)
  .then(({ data }) => {
    let count = 0;
    const results = data.results;
    results.forEach(film => {
      film.characters.forEach(char => {
        if (char.includes('18')) count++;
      });
    });
    console.log(count);
  })
  .catch(err => console.log(err.message));
