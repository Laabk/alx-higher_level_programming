#!/usr/bin/node

const mynub = parseInt(process.argv[2]);
if (Number.isNaN(mynub)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + mynub);
}
