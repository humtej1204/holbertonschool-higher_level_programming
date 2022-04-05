#!/usr/bin/node
const num = process.argv.splice(2).map((z) => parseInt(z)).sort((a, b) => (a - b));
if (num.length < 2) console.log(0);
else console.log(num[num.length - 2]);
