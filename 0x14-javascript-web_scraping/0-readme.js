#!/usr/bin/node
let args = process.argv.slice(process.argv.length - 1)
let fs = require('fs');

fs.readFile(args.toString(), 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
