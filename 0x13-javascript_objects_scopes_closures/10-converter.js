#!/usr/bin/node
exports.converter = function (base) {
  return (elm) => (elm).toString(base);
};
