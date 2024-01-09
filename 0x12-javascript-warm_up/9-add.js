#!/usr/bin/node
function add (a, b) {
  return b + a;
}
console.log(add(Number(process.argv[2]), Number(process.argv[3])));
