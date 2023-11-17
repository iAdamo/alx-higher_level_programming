#!/usr/bin/node

const arr = require('./100-data').list;

const newArr = arr.map((x, index) => x * index++);

console.log(arr);
console.log(newArr);
