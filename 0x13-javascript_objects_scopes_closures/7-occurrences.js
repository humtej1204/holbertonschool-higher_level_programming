#!/usr/bin/node
function nbOccurences (list, searchElement) {
  const nb = list.reduce((ac, e) => e === searchElement ? ac + 1 : ac, 0);
  return nb;
}

exports.nbOccurences = nbOccurences;
