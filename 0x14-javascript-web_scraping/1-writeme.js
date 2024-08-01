#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const strToWrite = process.argv[3];

fs.writeFile(filePath, strToWrite, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
