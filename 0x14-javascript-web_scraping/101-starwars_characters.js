#!/usr/bin/node
const axios = require('axios');

const getChar = async (url) => {
  const name = await axios.get(url);
  return (name.data.name);
};

const getAll = async (url) => {
  const response = await axios.get(url);
  for (const character of response.data.characters) {
    const newCaracter = await getChar(character);
    console.log(newCaracter);
  }
};

getAll(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`);
