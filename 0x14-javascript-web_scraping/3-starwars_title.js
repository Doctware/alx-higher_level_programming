#!/usr/bin/node

const rq = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

rq.get(url, function (err, resp, bdy) {
  if (err) {
    console.log(err);
  } else {
    const film = JSON.parse(bdy);
    console.log(`${film.title}`);
  }
});
