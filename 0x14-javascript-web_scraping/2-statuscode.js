#!/usr/bin/node

const rq = require('request');

rq.get(process.argv[2], function (err, resp, bdy) {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${resp.statusCode}`);
  }
});
