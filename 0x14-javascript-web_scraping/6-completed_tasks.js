#!/usr/bin/node

const rq = require('request');
const url = process.argv[2];

rq.get(url, function (err, resp, bdy) {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(bdy);
    const userCompletedTask = {};

    for (let i = 0; i < todos.length; i++) {
      const todo = todos[i];
      if (todo.completed) {
        if (!userCompletedTask[todo.userId]) {
          userCompletedTask[todo.userId] = 0;
        }
        userCompletedTask[todo.userId]++;
      }
    }
    console.log(JSON.stringify(userCompletedTask, null, 2));
  }
});
