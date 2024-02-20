#!/usr/bin/node
// characters of star war

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (erro, response, body) => {
  if (erro) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
    // console.log(characters);
    for (const character of characters) {
      request.get(character, (erro, response, body) => {
        if (erro) {
          console.log(erro);
        } else {
          const names = JSON.parse(body);
          console.log(names.name);
        }
      });
    }
  }
});
