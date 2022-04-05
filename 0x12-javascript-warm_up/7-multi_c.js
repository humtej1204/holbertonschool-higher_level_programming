#!/usr/bin/node
const numberOfTimes = parseInt(process.argv[2]);
if (isNaN(numberOfTimes)) console.log('Missing number of occurrences');
else {
  for (let i = 0; i < numberOfTimes; i++) console.log('C is fun');
}
