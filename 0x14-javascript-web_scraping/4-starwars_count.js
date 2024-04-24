#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18'; // ID of Wedge Antilles

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
  const count = films.filter(film => film.characters.includes(`/${characterId}/`)).length;
  //const count = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)).length;

  console.log(count);
});