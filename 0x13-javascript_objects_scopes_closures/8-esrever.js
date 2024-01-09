#!/usr/bin/node
// reverse a list
exports.esrever = function (list) {
  const reversedList = [];
  for (let d = list.length - 1; d >= 0; d--) {
    reversedList.push(list[d]);
  }
  return (reversedList);
};
