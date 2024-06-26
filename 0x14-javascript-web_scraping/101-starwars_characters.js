#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  const movie = JSON.parse(body);
  const charactersUrls = movie.characters;

  // Function to fetch character details
  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (charError, charResponse, charBody) => {
        if (charError) {
          reject(new Error(charError));
          return;
        }
        if (charResponse.statusCode !== 200) {
          reject(new Error(`Error: ${charResponse.statusCode}`));
          return;
        }
        const character = JSON.parse(charBody);
        resolve(character.name);
      });
    });
  };

  // Fetch and print character names
  Promise.all(charactersUrls.map(fetchCharacter))
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(err => {
      console.error('Error fetching characters:', err);
    });
});
