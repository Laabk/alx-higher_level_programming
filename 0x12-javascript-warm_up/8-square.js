#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else if (parseInt(process.argv[2]) > 0) {
  for (let d = 0; d < parseInt(process.argv[2]); d++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
