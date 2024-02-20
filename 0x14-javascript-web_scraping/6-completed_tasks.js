#!/usr/bin/node
// taskes commpleted by the user

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (ero, response, body) => {
  if (ero) {
    console.log(ero);
    return;
  }

  const tasksCompleted = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId] = 1;
      } else {
        tasksCompleted[todo.userId] += 1;
      }
    }
  });
  console.log(tasksCompleted);
});
