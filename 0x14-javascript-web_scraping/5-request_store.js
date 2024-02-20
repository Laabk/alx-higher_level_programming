#!/usr/bin/node
// contents in a webpage

const request = require('request');
const fs = require('fs');

request.get(process.argv[2], (ero, response, body) => {
  if (ero) {
    console.log(ero);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', (ero) => {
      if (ero) {
        console.log(ero);
      }
    });
  }
});
