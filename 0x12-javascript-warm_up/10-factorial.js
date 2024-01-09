#!/usr/bin/node
const numbe = Number(process.argv[2]);
function factorial (numbe) {
  if (numbe === 0 || isNaN(numbe)) {
    return (1);
  }
  return (numbe * factorial(numbe - 1));
}
console.log(factorial(numbe));
