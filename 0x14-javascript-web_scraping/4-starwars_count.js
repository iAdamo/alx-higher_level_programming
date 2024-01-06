#!/usr/bin/node
/**
 * a script that prints the number of movies where the character “Wedge Antilles” is present.
 */

const request = require('request');

const url = process.argv[2];
if (!url) {
  console.error('Please provide API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (const film of films) {
    for (const character of film.characters) {
      if (character.endsWith('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
