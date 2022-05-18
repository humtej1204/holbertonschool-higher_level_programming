#!/usr/bin/node
const args = process.argv.slice(process.argv.length - 1);
const fs = require('fs');

fs.readFile(args.toString(), 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
