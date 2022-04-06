#!/usr/bin/node
exports.logMe = function (item) {
  const { env } = require('process');
  env.nbPrinted = !env.nbPrinted ? 0 : parseInt(env.nbPrinted) + 1;
  console.log(`${process.env.nbPrinted}: ${item}`);
};
