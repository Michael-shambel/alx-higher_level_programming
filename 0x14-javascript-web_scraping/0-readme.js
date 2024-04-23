#!/usr/bin/node

const fs = require('fs');
//import fs module
const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
//read the content of the file

  if (err) {
    //if error occur the error parameter will contain 
    console.error('Error reading the file:', err);
    process.exit(1)		
	}
    //console log the content parameter
    console.log(data);
});

