#!/usr/bin/node
const { argv } = require('node:process');
const num = parseInt(argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let square = '';
    for (let j = 0; j < num; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
