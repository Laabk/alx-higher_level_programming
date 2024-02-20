#!/usr/bin/node
//status of a get requst

const request = require('request');
const url = process.argv[2];

request.get(url, (erro, response) => {
  if (erro) {
    console.log(erro);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
