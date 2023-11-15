#!/usr/bin/node
/**
 * script that searches the second biggest integer in the list of arguments.
 */
function secondBiggest (args) {
  // convert all value in the list to integers
  const integers = args.map(arg => +arg);
  // remove all dublicates and sort in descending order
  const sortedUniqueInt = [...new Set(integers)].sort((a, b) => b - a);
  // check if the arguments are more than one
  if (sortedUniqueInt.length < 2) {
    return (0);
  }

  // return the second biggest integer
  return (sortedUniqueInt[1]);
}

console.log(secondBiggest(process.argv.slice(2)));
