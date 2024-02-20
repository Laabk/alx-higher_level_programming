#!/usr/bin/node
// writing a string to file

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8',
  function (erro) {
    if (erro) {
      console.log(erro);
    }
  });
