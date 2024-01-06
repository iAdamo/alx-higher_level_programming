#!/usr/bin/node
/**
 * a script that gets the contents of a webpage and stores it in a file.
 * Created by Adam Sanusi Babatunde on 2024/01/06.
 */

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];
if (!filePath) {
  console.error('Please provide an URL to request and a file path to store the body response');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
