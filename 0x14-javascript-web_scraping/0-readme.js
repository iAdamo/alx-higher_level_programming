#!/usr/bin/node

const file = require('fs');

const filePath = process.argv[2];
if (!filePath) {
  console.error('Please specify a filepath');
  process.exit(1);
}
file.readFile(filePath, 'utf-8', (error, content) => {
  console.log(error || content);
});
