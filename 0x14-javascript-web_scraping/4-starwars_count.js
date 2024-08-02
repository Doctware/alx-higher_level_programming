#!/usr/bin/node

const rq = require('request');

const apiUrl = process.argv[2];
const chrUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

rq.get(apiUrl, function (err, resp, bdy) {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(bdy).results;
    let count = 0;

    for (let i = 0; i < films.length; i++) {
      const film = films[i];
      if (film.characters.includes(chrUrl)) {
        count = count + 1;
      }
    }
    console.log(count);
  }
});
