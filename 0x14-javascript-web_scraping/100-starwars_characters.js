#!/usr/bin/node
/**
 * a script that prints all characters of a Star Wars movie
 */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});

/* request(url, async function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const characters = JSON.parse(body).characters;
      for (const character of characters) {
        await new Promise(function (resolve, reject) {
          request(character, function (error, response, body) {
            if (error) {
              console.log(error);
            } else {
              console.log(JSON.parse(body).name);
            }
            resolve();
          });
        });
      }
    }
  });

  const axios = require('axios');

async function getCharacterNames() {
  try {
    const { data: film } = await axios.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`);
    for (const characterUrl of film.characters) {
      const { data: character } = await axios.get(characterUrl);
      console.log(character.name);
    }
  } catch (error) {
    console.error(error);
  }
}

getCharacterNames(); */
