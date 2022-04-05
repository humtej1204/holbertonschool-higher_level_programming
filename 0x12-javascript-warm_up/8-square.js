#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (isNaN(num)) console.log('Missing size');
else {
  let v = '';
  for (let i = 0; i < num; i++) v += 'X';
  v.split('').forEach(() => console.log(v));
}
