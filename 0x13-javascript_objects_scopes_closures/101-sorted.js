#!/usr/bin/node
const dict = require('./101-data').dict;

const [listValues, listKeys] = [Object.values(dict), Object.keys(dict)];
const newDict = {};

for (const key of listValues) {
  newDict[key] = listKeys.filter((value) => dict[value] === key);
}

console.log(newDict);
