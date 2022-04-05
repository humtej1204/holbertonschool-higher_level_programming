#!/usr/bin/node
let num = parseInt(process.argv[2]);
function fact (num) {
  if (num > 0) return (num * fact(num - 1));
  return (1);
}
if (isNaN(num)) num = 1;
console.log(fact(num));
