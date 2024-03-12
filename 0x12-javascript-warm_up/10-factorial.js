#!/usr/bin/node
const { argv } = require('node:process');
function factorial (n) {
  if (n <= 1) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
}
const num1 = parseInt(argv[2]);
if (isNaN(num1)) {
  console.log(1);
} else {
  const ans = factorial(num1);
  console.log(ans);
}
