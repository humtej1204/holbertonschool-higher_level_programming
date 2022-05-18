#!/usr/bin/node
const axios = require('axios');
const id = process.argv.slice(process.argv.length - 1);
const url = `https://swapi-api.hbtn.io/api/films/${id}/`;

axios.get(url).then(res => {
  const dat = res.data.characters;

  dat.forEach(x => {
    axios.get(x).then(d => {
      const dat = d.data.name;
      console.log(dat);
    });
  });
  /* console.log(res.data); */
});
