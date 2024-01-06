#!/usr/bin/node
/**
 *  a script that prints all characters of a Star Wars movie
 * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name by line in the same order of the list “characters” in the /films/ response
 */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      const res = await new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
      console.log(res);
    }
  }
});
