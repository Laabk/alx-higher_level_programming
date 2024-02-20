#!/usr/bin/node
// number of characters present in a movie ID
const request = require('request');
const url = process.argv[2];
const characterId = '18';
let numbs = 0;

request.get(url, (erro, response, body) => {
  if (erro) {
    console.log(erro);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(characterId)) {
          numbs += 1;
        }
      });
    });
    console.log(numbs);
  }
});
