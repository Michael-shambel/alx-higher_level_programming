#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  const films = JSON.parse(body).results;

  // Count occurrences of character with ID 18 in films array
  const count = films.reduce((count, film) => {
    return film.characters.includes(characterUrl) ? count + 1 : count;
  }, 0);

  console.log(count);
});
