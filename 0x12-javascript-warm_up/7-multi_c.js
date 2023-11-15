#!/usr/bin/node
/**
 * script that prints x times “C is fun”
 */
let times = parseInt(process.argv[2]); // can use +process.argv[2]

if (!isNaN(times)) {
  for (; times > 0; times--) {
    console.log('C is fun');
  }
} else if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
}
