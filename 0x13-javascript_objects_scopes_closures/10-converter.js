#!/usr/bin/Node
exports.converter = function (base) {
  return numbe => numbe.toString(base);
};
