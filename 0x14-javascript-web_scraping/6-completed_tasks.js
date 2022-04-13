#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

const args = process.argv;
const url = args[2];
const request = require('request');
request(url, (error, response, body) => {
  if (error) {
    console.log('error:', error);
  } else {
    const tasks = JSON.parse(body);
    const taskdict = {};
    for (let i = 0; i < tasks.length; i++) {
      if (tasks[i].completed === true) {
        if (taskdict[tasks[i].userId] === undefined) {
          taskdict[tasks[i].userId] = 1;
        } else {
          taskdict[tasks[i].userId]++;
        }
      }
    }
    console.log(taskdict);
  }
});
