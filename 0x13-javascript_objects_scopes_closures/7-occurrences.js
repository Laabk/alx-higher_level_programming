#!/usr/bin/node
// the searchelement
exports.nbOccurences = function (list, searchElement) {
  return list.filter(ele => ele === searchElement).length;
};
