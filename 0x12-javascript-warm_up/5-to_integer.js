#!/usr/bin/node
const args = process.argv.slice(2);
const fArg = args[0];
const number = parseInt(fArg, 10);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`my number: ${number}`);
}
