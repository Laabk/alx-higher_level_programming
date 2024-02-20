#!/usr/bin/node
// the title Star Wars
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(url, (erro, response, body) => {
  if (erro) {
    console.log(erro);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
