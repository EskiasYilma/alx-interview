#!/usr/bin/node

const r = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const params = { json: true };

r(url, params, async function (error, res, body) {
  if (error) {
    console.log(error);
  }
  for (const i of body.characters) {
    const charFunc = () => {
      return new Promise((resolve, reject) => {
        r(i, params, function (error, res, body) {
          if (error) {
            console.log(error);
          } else {
            resolve(body.name);
          }
        });
      });
    };
    console.log(await charFunc());
  }
});
