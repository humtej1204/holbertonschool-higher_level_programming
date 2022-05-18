#!/usr/bin/node
const process = require('process');
const axios = require('axios').default;

const URL = process.argv[2];

axios.get(URL, {
}).then(response => {
  const todo = response.data;
  const usersWithCompTasks = {};
  for (let i = 0; i < todo.length; i++) {
    if (todo[i].completed === true) {
      const key = todo[i].userId;
      if (usersWithCompTasks[key] === undefined) {
        usersWithCompTasks[key] = 1;
      } else {
        let currTasks = usersWithCompTasks[key];
        currTasks += 1;
        usersWithCompTasks[key] = currTasks;
      }
    }
  }
  console.log(usersWithCompTasks);
}).catch(error => {
  if (error) {
    console.log(error.message);
  }
});
