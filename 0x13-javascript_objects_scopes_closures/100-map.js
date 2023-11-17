#!/usr/bin/node

const arr = require('./100-data').list; // modify the path to ./maintest/100-data to run

const newArr = arr.map((x, index) => x * index++);

console.log(arr);
console.log(newArr);
