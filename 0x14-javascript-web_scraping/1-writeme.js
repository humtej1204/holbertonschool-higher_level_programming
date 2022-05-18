#!/usr/bin/node
const args = process.argv.slice(process.argv.length - 2);
const fs = require('fs');

const content = args[1];

fs.writeFile(args[0], content, 'utf8', err => {
  if (err) {
    console.error(err);
  }
});
