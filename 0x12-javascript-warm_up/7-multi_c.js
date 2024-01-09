#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of ocurrences');
} else {
  for (let d = 0; d < parseInt(process.argv[2]); d++) {
    console.log('C is fun');
  }
}
