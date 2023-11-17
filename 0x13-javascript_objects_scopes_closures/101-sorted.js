#!/usr/bin/node

const dicts = require('./maintest/101-data').dict;

const newDict = {};

for (const key in dicts) {
  if (!newDict[dicts[key]]) {
    newDict[dicts[key]] = [];
  }
  newDict[dicts[key]].push(key);
}
console.log(newDict);
