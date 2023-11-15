#!/usr/bin/node
/**
 * script that computes and prints a factorial
 */
function factorial (num) {
  if (num === 0 || isNaN(num)) {
    return (1);
  } else {
    return (factorial(num - 1) * num);
  }
}

const num = +process.argv[2];
console.log(factorial(num));
