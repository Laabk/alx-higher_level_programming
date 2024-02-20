#!/usr/bin/node
// Read and prints contnt from file

const filesys = require('fs');
filesys.readFile(process.argv[2], 'utf-8',
  function (erro, data) {
    if (erro) {
      console.log(erro);
      return;
    }
    console.log(data);
  });
