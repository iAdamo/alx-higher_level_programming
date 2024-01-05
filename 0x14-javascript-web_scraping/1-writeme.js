#!/usr/bin/node
/**
 * a script that writes a string to a file.
 */
const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];
if (!filePath) {
  console.error('Please specify a filepath and string content');
  process.exit(1);
}
fs.writeFile(filePath, content, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
