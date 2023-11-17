#!/usr/bin/node

const dicts = require('./101-data').dict; // modify the path to ./maintest/101-data to run

const newDict = {};

for (const key in dicts) {
  if (!newDict[dicts[key]]) {
    newDict[dicts[key]] = [];
  }
  newDict[dicts[key]].push(key);
}
console.log(newDict);
