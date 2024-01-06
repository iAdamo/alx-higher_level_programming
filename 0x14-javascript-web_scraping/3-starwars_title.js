#!/usr/bin/node
/**
 * a script that prints the title of a Star Wars movie
 * where the episode number matches a given integer.
 */

const request = require('request');

const id = process.argv[2];
if (!id) {
  console.error('Please provide an id');
  process.exit(1);
}

const url = `https://swapi-api.hbtn.io/api/films/${id}`;
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  console.log(JSON.parse(body).title);
});
