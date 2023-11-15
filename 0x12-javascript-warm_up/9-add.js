#!/usr/bin/node
/**
 * script that prints the addition of 2 integers
 */
function add (a, b) {
  return (a + b);
}

const firstArg = +process.argv[2];
const secondArg = +process.argv[3];

console.log(add(firstArg, secondArg));
