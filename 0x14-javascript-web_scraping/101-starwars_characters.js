#!/usr/bin/node
const axios = require('axios').default;
const ID = process.argv[2];

async function getNameChar (url) {
  const data = await axios.get(url);
  const { name } = data;
  return name;
}

async function getCharsOfFilms (id = ID) {
  const url = `https://swapi-api.hbtn.io/api/films/${id}`;

  const data = await axios.get(url);
  const { characters } = data;
  for (const char of characters) {
    const name = await getNameChar(char);
    console.log(name);
  }
}

getCharsOfFilms(ID);
