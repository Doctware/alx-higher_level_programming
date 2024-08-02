#!/usr/bin/node

const rq = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

rq.get(url, function (err, resp, bdy) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filePath, bdy, 'utf8', function (err, data) {
      if (err) {
        console.log(err);
      }
    });
  }
});
