#!/usr/bin/node
/**
 * a script that computes the number of tasks completed by user id.
 */

const request = require('request');

const url = process.argv[2];
if (!url) {
  console.error('Please provide API URL: https://jsonplaceholder.typicode.com/todos');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  const tasks = JSON.parse(body);
  const completedTasks = {};
  for (const task of tasks) {
    if (task.completed) {
      if (completedTasks[task.userId]) {
        completedTasks[task.userId]++;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  }
  console.log(completedTasks);
});
